from .models import Comment, Suggestions
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