from django.conf.urls import url
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from users.models import Profile, CustomUser
from blogs.models import Post
from django.views.generic import TemplateView
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, ProfileEditForm
from django.urls import reverse
from django.contrib import messages


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
    # page_user = request.user
    # user_profile =  get_object_or_404(Profile, page_user=page_user)

    # if request.method == "POST":
    #     form = CustomUserChangeForm(request.POST)
    #     if form.is_valid():
            

# class ProfileView(generic.DetailView):
#     model = Profile
#     template_name = 'users/profile.html'

#     def get_context_data(self, **kwargs):
#         context = super(ProfileView, self).get_context_data(**kwargs)

#         page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        
#         context['page_user'] = page_user
       
#         context['user_posts'] = page_user.user.author_posts.all()
#         context['user_fav_posts'] = page_user.user.favourite.all()
        
#         context['post_num'] = Post.published.count()
#         # context['project_num'] = Project.objects.count()
#         context['most_recent'] = Post.published.all().order_by('-timestamp', '-updated')[:3]
#         context['post_by_category_count']  = Post.published.values('categories__title').annotate(Count('categories__title')).order_by('categories')
#         return context
