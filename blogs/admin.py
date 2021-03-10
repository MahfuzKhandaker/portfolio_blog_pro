from django.contrib import admin

from .models import Post, Category, Tag, Comment

from blogs.forms import AdminPostForm

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'timestamp', 'updated')
    list_filter = ('timestamp', 'updated')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    form = AdminPostForm
    fields = ['title', 'slug', 'author', 'categories', 'overview', 'content', 'thumbnail', 'image_caption', 'likes', 'featured', 'tags', 'status']
    

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)