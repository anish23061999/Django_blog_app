from .models import Post, Comment
from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):

    model = User
    author = Post.author
    class Meta:
        model = Comment
        fields = ('author', 'text',)