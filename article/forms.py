from .models import Category, Comment, Post, Suggestions
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestions
        fields = ('proposed_content', 'reason')
        labels = {
            'proposed_content': 'Suggested article content',
            'reason': 'Reason for suggestion',
        }
        widgets = {
            'proposed_content': SummernoteWidget(),
            'reason': forms.Textarea(attrs={'rows': 4}),
        }


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'featured_image', 'content', 'categories',
                  'status', 'excerpt')
        widgets = {
            'content': SummernoteWidget(),
            'excerpt': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].help_text = (
            'To select multiple categories hold down ctrl then choose the categories'
        )
        self.fields['featured_image'].widget.attrs['accept'] = (
            'image/jpeg,image/png,image/webp,image/gif'
        )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)