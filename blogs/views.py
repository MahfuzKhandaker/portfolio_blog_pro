from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import FormView, CreateView, ListView, DetailView
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
from .forms import PostForm, CommentForm
from blogs.utils import get_read_time
from .models import Post, Comment, Category
from .mixins import AjaxFormMixin
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Count
from django.db.models import Q
try:
    from django.utils import simplejson as json
except ImportError:
    import json


# class JoinFormView(AjaxFormMixin, FormView):
#     form_class = JoinForm
#     template_name  = 'forms/ajax.html'
#     success_url = '/form-success/'


class PostCreateView(AjaxFormMixin, CreateView):
    form_class = PostForm
    template_name = 'blogs/create_post.html'



class PostListView(ListView):
    model = Post
    template_name = 'blogs/post_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['posts'] = Post.published.order_by('-timestamp')
        context['post_num'] = Post.published.count()
        context['most_recent'] = Post.published.order_by('-timestamp')[:3]
        context['post_by_category_count']  = Post.published.values('categories__title').annotate(Count('categories__title')).order_by('categories')
        return context


class SearchResultsListView(ListView):
    model = Post
    template_name = 'blogs/search_results.html'
    context_object_name = 'searching_post_list'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.published.filter(
            Q(title__icontains=query) | Q(categories__title__icontains=query)
        )

def post_category(request, category):
    category_posts = Post.published.filter(
        categories__title__contains=category
    ).order_by(
        '-timestamp'
    )
    context = {
        'category': category,
        'category_posts': category_posts
    }
    return render(request, 'blogs/post_category.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
    
    is_liked = False
    is_favourite = False

    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    if post.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    if request.method=='POST':
        querydict = request.POST
        comment_form = CommentForm(querydict)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.reply_id = querydict.get('comment_id')
            comment.save()
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'is_liked': is_liked,
        'is_favourite': is_favourite,
        'comments': comments,
        'total_likes': post.likes.count(),
        'total_comments': post.comments.count(),
        'comment_form': comment_form,
    }
    if request.is_ajax():
        html = render_to_string('blogs/comment_section.html', context, request=request)
        comments = serializers.serialize('json', list(comments), fields=('content', 'reply', 'post', 'user__username'))
        return JsonResponse({'form': html, 'comments': comments})

    return render(request, 'blogs/post_detail.html', context)

def post_favourite_list(request):
    user = request.user
    favourite_posts = user.favourite.all()
    context = {
        'favourite_posts': favourite_posts,
    }
    return render(request, 'blogs/post_favourite_list.html', context)

def favourite_post(request):
    post = get_object_or_404(Post, slug=request.POST.get('post_slug'))
    is_favourite = False
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
        is_favourite = False
    else:
        post.favourite.add(request.user)
        is_favourite = True
    context ={
        'post': post,
        'is_favourite': is_favourite,
    }
    if request.is_ajax():
        html = render_to_string('blogs/favourite_section.html', context, request=request)
        return JsonResponse({'form': html})


def likes(request):
    post = get_object_or_404(Post, slug=request.POST.get('post_slug'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    context ={
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.likes.count(),
    }
    if request.is_ajax():
        html = render_to_string('blogs/like_section.html', context, request=request)
        return JsonResponse({'form': html})