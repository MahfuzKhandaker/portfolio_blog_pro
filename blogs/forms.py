from django import forms
from pagedown.widgets import  PagedownWidget, AdminPagedownWidget
from .models import Post, Comment, Tag


class AdminPostForm(forms.ModelForm):
    content =  forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'category', 'overview', 'content', 'thumbnail', 'image_caption', 'likes', 'featured', 'tags', 'status']

class PostForm(forms.ModelForm):
    content =  forms.CharField(widget=PagedownWidget())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'category', 'overview', 'content', 'thumbnail', 'image_caption', 'likes', 'featured', 'tags', 'status']

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