from django.urls import path
from users import views

urlpatterns = [
    path('<username>/', views.profile, name='profile'),
    path('<username>/update/', views.profile_update, name='profile_update'),
]