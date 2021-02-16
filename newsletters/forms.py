from django import forms
from pagedown.widgets import PagedownWidget
from .models import NewsletterUser, Newsletter

class NewsUserForm(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

class NewsletterCreationForm(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget(attrs={'rows':5, 'cols':10}))
    class Meta:
        model = Newsletter
        fields = ['subject', 'body', 'email', 'status']