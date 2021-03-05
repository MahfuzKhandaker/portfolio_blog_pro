from django.urls import path
from users.views import ProfileView

urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='user_profile'),
    # path('<int:pk>/', project_detail, name='project_detail')
]