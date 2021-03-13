from django.contrib import admin

from .models import Post, Category, Tag, Comment

from blogs.forms import AdminPostForm

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'updated')
    list_filter = ('timestamp', 'updated')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)
    # raw_id_fields = ('tags',)
    form = AdminPostForm
    fields = ['title', 'slug', 'author', 'category', 'overview', 'content', 'thumbnail', 'image_caption', 'likes', 'featured', 'tags', 'status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)