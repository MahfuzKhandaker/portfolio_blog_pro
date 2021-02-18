from django.urls import path
from blogs.views import PostCreateView, PostListView, SearchResultsListView, post_detail, favourite_post, post_favourite_list, likes, post_category


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('favourite_post/', favourite_post, name='favourite_post'),
    path('likes/', likes, name='likes'),
    path('favourites/', post_favourite_list, name='post_favourite_list'),
    path('<slug:slug>/', post_detail, name='post-detail'),
    path('<category>/', post_category, name="post_category"),
]