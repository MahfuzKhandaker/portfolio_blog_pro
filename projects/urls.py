from django.urls import path
from projects.views import project_index,  lazy_load_projects, project_detail

urlpatterns = [
    path('', project_index, name='project_index'),
    path('lazy_load_projects/', lazy_load_projects, name='lazy_load_projects'),
    path('<int:pk>/', project_detail, name='project_detail')
]