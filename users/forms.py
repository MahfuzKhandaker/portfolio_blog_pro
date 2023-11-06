from collections import UserString
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from users.models import CustomUser
from django.contrib.auth import authenticate

# from allauth.account.forms import SignupForm
# from django import forms

# class CustomSignupForm(SignupForm):
#     email = forms.EmailField(
#         label='email address',
#         max_length=255
#     )

#     def save(self, request):

#         # Ensure you call the parent class's save.
#         # .save() returns a User object.
#         user = super(CustomSignupForm, self).save(request)

#         # Add your own processing here.
#         user.email = self.cleaned_data['email']
#         user.save()

        

#         # You must return the original result.
#         return user


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            customuser = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % customuser)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            customuser = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % customuser)


# class AccountAuthenticationForm(forms.ModelForm):
# 	password = forms.CharField(label='Password', widget=forms.PasswordInput)

# 	class Meta:
# 		model = get_user_model()
# 		fields = ('email', 'password')

# 	def clean(self):
# 		if self.is_valid():
# 			email = self.cleaned_data['email']
# 			password = self.cleaned_data['password']
# 			if not authenticate(email=email, password=password):
# 				raise forms.ValidationError("Invalid login")


class CustomUserUpdateForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'photo', 'bio', 'location', 'website_url', 'facebook_url', 'twitter_url', 'linkedin_url', 'github_url', 'youtube_url')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            customuser = CustomUser.objects.exclude(pk=self.instance.pk).get(email=email)
        except CustomUser.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % customuser)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            customuser = CustomUser.objects.exclude(pk=self.instance.pk).get(username=username)
        except CustomUser.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % customuser)

    def save(self, commit=True):
        user_account = super(CustomUserUpdateForm, self).save(commit=False)
        user_account.username = self.cleaned_data['username']
        user_account.email = self.cleaned_data['email'].lower()
        user_account.photo = self.cleaned_data['photo']
        user_account.bio = self.cleaned_data['bio']
        user_account.location = self.cleaned_data['location']
        user_account.website_url = self.cleaned_data['website_url']
        user_account.facebook_url = self.cleaned_data['facebook_url']
        user_account.twitter_url = self.cleaned_data['twitter_url']
        user_account.linkedin_url = self.cleaned_data['linkedin_url']
        user_account.github_url = self.cleaned_data['github_url']
        user_account.youtube_url = self.cleaned_data['youtube_url']

        if commit:
            user_account.save()
            return user_account
