from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from users.models import Profile, CustomUser
from blogs.models import Post
from django.views.generic import TemplateView
from django.db.models import Count


class ProfileView(generic.DetailView):
    model = Profile
    # context_object_name = 'posts'
    template_name = 'users/profile.html'
    paginate_by = 3


    def get_context_data(self, **kwargs):
        # user_profile = Profile.objects.all()
        context = super(ProfileView, self).get_context_data(**kwargs)

        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])

        context['page_user'] = page_user
        context['user_posts'] = page_user.user.author_posts.all()
        context['user_fav_posts'] = page_user.user.favourite.all()
    #     user = request.user
    # favourite_posts = user.favourite.all()
        
        # context['post_num'] = Post.published.count()
        # context['project_num'] = Project.objects.count()
        # context['most_recent'] = Post.published.all().order_by('-timestamp', '-updated')[:3]
        # context['post_by_category_count']  = Post.published.values('categories__title').annotate(Count('categories__title')).order_by('categories')
        return context
