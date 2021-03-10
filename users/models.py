from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='profile/', blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    website_url = models.URLField(max_length = 255, blank=True)
    facebook_url = models.URLField(max_length = 255, blank=True)
    tweeter_url = models.URLField(max_length = 255, blank=True)
    linkedin_url = models.URLField(max_length = 255, blank=True)
    instagram_url = models.URLField(max_length = 255, blank=True)
    pinterest_url = models.URLField(max_length = 255, blank=True)

    objects = models.Manager()


    def __str__(self):
        return self.user.username

    class Meta:
        ordering = ['-dob']
        # verbose_name_plural = 'profiles'

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()