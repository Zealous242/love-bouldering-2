from django.contrib import admin
from django import forms
from .models import Category, Comment, Post, Suggestions
from django_summernote.admin import SummernoteModelAdmin


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['featured_image'].widget.attrs['accept'] = (
            'image/jpeg,image/png,image/webp,image/gif'
        )


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    form = PostAdminForm
    list_display = ('title', 'category_list', 'slug', 'status', 'author', 'created_on', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('categories', 'status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}  
    summernote_fields = ('content',)

    @admin.display(description='categories')
    def category_list(self, post):
        return ', '.join(category.name for category in post.categories.all())

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['featured_image'].widget.attrs['accept'] = (
            'image/jpeg,image/png,image/webp,image/gif'
        )
        return form

    class Media:
        css = {'all': ('css/admin_comments.css',)}
        js = ('js/admin_posts.js',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'approved', 'created_on')
    list_filter = ('post__title', 'author', 'approved', 'created_on')

    class Media:
        css = {'all': ('css/admin_comments.css',)}
        js = ('js/admin_comments.js',)


@admin.register(Suggestions)
class SuggestionsAdmin(SummernoteModelAdmin):
    list_display = ('post', 'submitted_by', 'status', 'created_on', 'updated_on')
    list_filter = ('status', 'created_on')
    search_fields = ('post__title', 'submitted_by__username', 'proposed_content')
    summernote_fields = ('proposed_content',)