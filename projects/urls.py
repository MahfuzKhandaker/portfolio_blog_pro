from django.urls import path
from projects.views import project_index, project_detail

urlpatterns = [
    path('', project_index, name='project_index'),
    path('<int:pk>/', project_detail, name='project_detail')
]