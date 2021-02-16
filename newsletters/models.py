from django.db import models

class NewsletterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "NewsletterUsers"

    def __str__(self):
        return self.email
        
    objects = models.Manager()


class Newsletter(models.Model):
    EMAIL_STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    subject = models.CharField(max_length=250)
    body    = models.TextField()
    email   = models.ManyToManyField(NewsletterUser)
    status  = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    objects = models.Manager()

    class Meta:
        permissions = [
            ('special_status', 'can read all newsletter'),
        ]

    def __str__(self):
        return self.subject
