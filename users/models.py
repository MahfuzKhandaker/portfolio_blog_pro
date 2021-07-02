from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image

class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(default='default.jpg', upload_to='profile', blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    website_url = models.URLField(max_length = 255, blank=True)
    facebook_url = models.URLField(max_length = 255, blank=True)
    twitter_url = models.URLField(max_length = 255, blank=True)
    linkedin_url = models.URLField(max_length = 255, blank=True)
    github_url = models.URLField(max_length = 255, blank=True)
    youtube_url = models.URLField(max_length = 255, blank=True)

    objects = models.Manager()


    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-dob']
        verbose_name_plural = 'profiles'


