from django.contrib import admin
from .models import Contact
from .forms import ContactForm

class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ('from_email', 'subject', 'message', 'created_at',)
    search_fields = ('from_email', 'subject',)

admin.site.register(Contact, ContactAdmin)
