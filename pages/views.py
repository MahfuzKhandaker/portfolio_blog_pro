from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from blogs.models import Post, Category
from projects.models import Project
from django.views.generic import TemplateView
from django.db.models import Count


class HomePageView(generic.ListView):
    model = Post
    # context_object_name = 'posts'
    template_name = 'pages/home.html'
    paginate_by = 6 


    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['featured_posts'] = Post.published.filter(featured=True)[:3]
        context['post_num'] = Post.published.count()
        context['project_num'] = Project.objects.count()
        context['most_recent'] = Post.published.all().order_by('-timestamp', '-updated')[:3]
        context['post_by_category_count']  = Post.published.values('category__title').annotate(Count('category__title')).order_by('category')
        return context


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
