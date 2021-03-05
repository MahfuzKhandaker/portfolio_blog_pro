from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils.safestring import mark_safe   
from blogs.utils import get_read_time


class Category(models.Model):
    title = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-title']
        verbose_name_plural = 'categories'

class Tag(models.Model):
    name = models.CharField(max_length=60, null=True)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    objects     = models.Manager()      #Default Manager
    published   = PublishedManager()  #Custom Model Manager

    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )

    title       = models.CharField(max_length=100)
    slug        = models.SlugField(null=False, unique=True)
    overview    = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    content     = models.TextField()
    author      = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_posts')
    thumbnail   = models.ImageField(upload_to='images/', blank=True)
    image_caption   = models.CharField(max_length=125, blank=True, null=True)
    categories  = models.ManyToManyField(Category)
    featured    = models.BooleanField()
    tags        = models.ManyToManyField(Tag)
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    likes       = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='likes')
    favourite   = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favourite', blank=True)
    number_of_views = models.IntegerField(default=0, null=True, blank=True)
    read_time       = models.IntegerField(default=0)
    
    class Meta: 
        ordering = ['-id']
        verbose_name_plural = 'posts'
 
    def __str__(self): 
        return self.title

    def total_likes(self):
        return self.likes.count()
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if instance.content:
        html_string = instance.content
        read_time_var = get_read_time(html_string)
        instance.read_time = read_time_var
pre_save.connect(pre_save_post_receiver, sender=Post)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=1000)
    reply = models.ForeignKey('Comment', on_delete=models.CASCADE, related_name='replies', null=True, blank=True, default=None)
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))

    class Meta: 
        ordering = ['-timestamp']
        verbose_name_plural = 'comments'

    