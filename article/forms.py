from .models import Category, Comment, Post, Suggestions
from django import forms
from django_summernote.widgets import SummernoteWidget
import re


class HTML5SummernoteWidget(SummernoteWidget):
    def render(self, name, value, attrs=None, **kwargs):
        rendered = super().render(name, value, attrs, **kwargs)
        rendered = rendered.replace(
            '<style>\niframe.note-fullscreen {\n'
            '  position: fixed;\n'
            '  top: 0;\n'
            '  left: 0;\n'
            '  width: 100vw!important;\n'
            '  height: 100vh!important;\n'
            '  z-index: 4000;\n'
            '}\n</style>\n',
            '',
        )
        rendered = re.sub(
            r'<div class="summernote-div"\s+class="([^"]*)"',
            r'<div class="summernote-div \1"',
            rendered,
        )
        rendered = re.sub(
            r'<div\b[^>]*class="([^"]*summernote-div[^"]*)"[^>]*>',
            r'<div class="\1">',
            rendered,
        )
        rendered = rendered.replace(' frameborder="0"', '')
        return rendered.replace('hidden="true"', 'hidden')


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
            'content': HTML5SummernoteWidget(),
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