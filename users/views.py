from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserUpdateForm
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
        user_form = CustomUserUpdateForm(data=request.POST or None, instance=request.user, files=request.FILES)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', request.user.username)
    else:
        user_form = CustomUserUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
    }
    return render(request, 'users/edit_profile.html', context)