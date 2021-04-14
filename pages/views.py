from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from blogs.models import Post, Category
from projects.models import Project
from django.views.generic import TemplateView
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core import serializers


class HomePageView(generic.ListView):
    model = Post
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['featured_posts'] = Post.published.filter(featured=True)[:4]
        # paginator = Paginator(context['featured_posts'], 3)
        # page = self.request.GET.get('page')
        # try:
        #     context['featured_posts'] = paginator.page(page)
        # except PageNotAnInteger:
        #     context['featured_posts'] = paginator.page(1)
        # except EmptyPage:
        #     context['featured_posts'] = paginator.page(paginator.num_pages)

        context['post_num'] = Post.published.count()
        context['project_num'] = Project.objects.count()
        context['most_recent'] = Post.published.all().order_by('-timestamp', '-updated')[:3]
        context['post_by_category_count']  = Post.published.values('category__title').annotate(Count('category__title')).order_by('category')        

        if self.request.is_ajax():
            html = render_to_string('pagination.html', context, request=self.request)
            featured_posts = serializers.serialize('json', list(featured_posts))
            return JsonResponse({'form': html, 'featured_posts': featured_posts})

        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
