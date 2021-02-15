from django.db import models
from django.shortcuts import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', blank=True)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', args=[self.pk])