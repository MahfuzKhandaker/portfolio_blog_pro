from django.shortcuts import render
from projects.models import Project
from django.contrib.auth.decorators import login_required

@login_required
def project_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_index.html', {'projects': projects})
    

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)