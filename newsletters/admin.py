from django.contrib import admin

from newsletters.models import NewsletterUser, Newsletter

from newsletters.forms import NewsletterCreationForm


class NewsletterAdmin(admin.ModelAdmin):
    list_display =('subject', 'created') 
    form = NewsletterCreationForm 
    fields = ['subject', 'body', 'email', 'status']


class NewsletterUserAdmin(admin.ModelAdmin):
    list_display =('email', 'date_added')


admin.site.register(Newsletter, NewsletterAdmin)

admin.site.register(NewsletterUser, NewsletterUserAdmin)