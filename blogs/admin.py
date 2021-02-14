from django.contrib import admin

from .models import Author, Post, Profile, Category, Comment

from blogs.forms import PostForm

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'timestamp', 'updated')
    list_filter = ('timestamp', 'updated')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    form = PostForm
    fields = ['title', 'slug', 'author', 'categories', 'overview', 'content', 'thumbnail', 'image_caption', 'likes', 'featured', 'status']
    

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)