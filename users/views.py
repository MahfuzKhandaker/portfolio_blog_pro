from django.contrib.auth import get_user_model
from django.conf.urls import url
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
# from users.models import Profile, CustomUser
from blogs.models import Post
from django.views.generic import TemplateView
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileEditForm
from django.urls import reverse
from django.contrib import messages

CustomUser = get_user_model()

@login_required
def profile(request, username):
    page_user = CustomUser.objects.get(username=username)
    context = {
        'page_user': page_user, 
        'user_posts':page_user.author_posts.all(), 
        'user_fav_posts':page_user.favourite.all()
    }
    return render(request, 'users/profile.html', context)

@login_required
def profile_update(request, username):
    request.user = CustomUser.objects.get(username=username)
    if request.method == 'POST':
        user_form = CustomUserChangeForm(data=request.POST or None, instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None, instance=request.user.profile, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            print(profile_form)
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', request.user.username)
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'users/edit_profile.html', context)