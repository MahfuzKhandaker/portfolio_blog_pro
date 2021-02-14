from django import forms
from pagedown.widgets import AdminPagedownWidget
from .models import Post, Comment


class PostForm(forms.ModelForm):
    content =  forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Post
        fields = ('title', 'slug', 'overview', 'content', 'thumbnail', 
        'categories', 'featured')



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