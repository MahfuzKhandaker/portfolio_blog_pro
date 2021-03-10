from django import forms
from pagedown.widgets import  PagedownWidget, AdminPagedownWidget
from .models import Post, Comment


class AdminPostForm(forms.ModelForm):
    overview = forms.CharField(widget=AdminPagedownWidget())
    content =  forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'categories', 'overview', 'content', 'thumbnail', 'image_caption', 'likes', 'featured', 'tags', 'status']

class PostForm(forms.ModelForm):
    overview = forms.CharField(widget=PagedownWidget())
    content =  forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'categories', 'overview', 'content', 'thumbnail', 'image_caption', 'likes', 'featured', 'tags', 'status']

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Write Here!',
        'rows': '4',
        'cols': '50'
    }))
    class Meta:
        model = Comment
        fields = ('content',)