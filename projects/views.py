from django.shortcuts import render
from projects.models import Project
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required

@login_required
def project_index(request):
    projects = Project.objects.all()[:2]
    return render(request, 'projects/project_index.html', {'projects': projects})

def lazy_load_projects(request):
    page = request.POST.get('page')
    projects = Project.objects.all()
    project_per_page = 2
    paginator = Paginator(projects, project_per_page)
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(2)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
        
    projects_html = render_to_string(
        'projects/projects.html', 
        {'projects': projects}
    )
    output_data = {
        'projects_html': projects_html,
        'has_next': projects.has_next()
    }
    return JsonResponse(output_data)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)