from django.urls import path
from blogs.views import PostCreateView, PostListView, post_detail, favourite_post, post_favourite_list, likes


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('favourite_post/', favourite_post, name='favourite_post'),
    path('likes/', likes, name='likes'),
    path('favourites/', post_favourite_list, name='post_favourite_list'),
    path('<slug:slug>/', post_detail, name='post-detail'),
    path('create/', PostCreateView.as_view(), name='create-post'),
]