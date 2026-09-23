from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from requests import post
from .models import Category, Comment, Post, Suggestions
from .forms import CommentForm, PostCreateForm, SuggestionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.db.models import Q

# Create your views here.
def is_superuser(user):
    return user.is_authenticated and user.is_superuser


@user_passes_test(is_superuser)
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, 'Post created successfully.')
            return HttpResponseRedirect(reverse('post_detail', args=[post.slug]))
    else:
        form = PostCreateForm()

    return render(request, 'article/post_create.html', {'form': form})


@user_passes_test(is_superuser)
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Post updated successfully.')
            if post.status == 1:
                return HttpResponseRedirect(
                    reverse('post_detail', args=[post.slug])
                )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = PostCreateForm(instance=post)

    return render(request, 'article/post_edit.html', {'form': form, 'post': post})


class PostList(generic.ListView):
    template_name = "article/index.html"
    paginate_by = 6

    def get_queryset(self):
        queryset = Post.objects.filter(status=1).order_by("-created_on")
        category_id = self.request.GET.get("category")
        search_query = self.request.GET.get("q", "").strip()

        if category_id and category_id.isdigit():
            queryset = queryset.filter(categories__id=category_id)

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(excerpt__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(categories__name__icontains=search_query)
            )

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.order_by("name")
        context["selected_category"] = self.request.GET.get("category", "")
        context["search_query"] = self.request.GET.get("q", "")
        return context
    
def post_detail(request, slug):
    """
    Display an individual :model:`article.Post`.

    **Context**

    ``post``
        An instance of :model:`article.Post`.

    **Template:**

    :template:`article/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    
    comment_form = CommentForm()
    suggestion_form = SuggestionForm()

    return render(
        request,
        "article/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "suggestion_form": suggestion_form,
        },
    )


@login_required
def suggestion_create(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)

    if request.method == "POST":
        suggestion_form = SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            suggestion = suggestion_form.save(commit=False)
            suggestion.post = post
            suggestion.submitted_by = request.user
            suggestion.save()
            messages.success(
                request,
                'Your suggestion has been submitted for review.',
            )
        else:
            messages.error(request, 'Please correct the errors in your suggestion.')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def suggestion_list(request):
    suggestions = Suggestions.objects.filter(
        submitted_by=request.user
    ).select_related('post')
    return render(
        request,
        'article/suggestion_list.html',
        {
            'suggestions': suggestions,
            'suggestion_count': suggestions.count(),
        },
    )


@login_required
def suggestion_edit(request, suggestion_id):
    suggestion = get_object_or_404(
        Suggestions,
        pk=suggestion_id,
        submitted_by=request.user,
    )

    if request.method == 'POST':
        form = SuggestionForm(request.POST, instance=suggestion)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.status = 'pending'
            suggestion.save()
            messages.success(request, 'Your suggestion was updated and sent for review.')
            return HttpResponseRedirect(reverse('suggestion_list'))
    else:
        form = SuggestionForm(instance=suggestion)

    return render(
        request,
        'article/suggestion_edit.html',
        {'form': form, 'suggestion': suggestion},
    )


@login_required
def suggestion_delete(request, suggestion_id):
    suggestion = get_object_or_404(
        Suggestions,
        pk=suggestion_id,
        submitted_by=request.user,
    )

    if request.method == 'POST':
        suggestion.delete()
        messages.success(request, 'Your suggestion was deleted.')

    return HttpResponseRedirect(reverse('suggestion_list'))
    
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                    'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))