from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from blogs.models import Post
from django.views.generic import TemplateView


class HomePageView(generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'pages/home.html'
    paginate_by = 6 


    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['posts'] = Post.published.all()
        context['post_num'] = Post.published.count()
        context['most_recent'] = Post.published.all().order_by('-timestamp', '-updated')[:3]
        return context



class AboutPageView(TemplateView): # new
    template_name = 'pages/about.html'
