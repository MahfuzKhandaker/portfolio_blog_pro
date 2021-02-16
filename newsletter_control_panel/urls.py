from django.urls import path
from newsletters.views import newsletter_control,  newsletter_control_edit, newsletter_control_delete, NewsletterListView, NewsletterDetailView


urlpatterns = [
    path('newsletter/', newsletter_control, name='newsletter'),
    path('newsletter-list/', NewsletterListView.as_view(), name='newsletter-list'),
    path('newsletter-detail/<int:pk>', NewsletterDetailView.as_view(), name='newsletter-detail'),
    path('newsletter-edit/<int:pk>', newsletter_control_edit, name='newsletter-edit'),
    path('newsletter-delete/<int:pk>', newsletter_control_delete, name='newsletter-delete'),
]