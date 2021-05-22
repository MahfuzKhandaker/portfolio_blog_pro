from django.urls import path
from blogs.views import post_create, post_list, lazy_load_posts, SearchResultsListView, post_detail, post_edit, favourite_post, post_favourite_list, likes, post_by_category, post_by_tag


urlpatterns = [
    path('', post_list, name='post-list'),
    path('lazy_load_posts/', lazy_load_posts, name='lazy_load_posts'),
    path('create/', post_create, name='create-post'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('favourite_post/', favourite_post, name='favourite_post'),
    path('likes/', likes, name='likes'),
    path('favourites/', post_favourite_list, name='post_favourite_list'),
    path('category/<slug:category_slug>/', post_by_category, name='post-by-category'),
    path('tag/<slug:tag_slug>/', post_by_tag, name='post-by-tag'),
    path('<slug:slug>/', post_detail, name='post-detail'),
    path('<slug:slug>/edit/', post_edit, name='post-edit'),
]