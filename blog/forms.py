from django import forms

from .models import Comment, Article


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('poster', 'content')

    exclude = ('article',)