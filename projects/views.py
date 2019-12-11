from django.shortcuts import render, get_object_or_404

from projects.models import Project


# Create your views here.


def projects_index(request):
    return render(request, 'project_index.html', {'projects': Project.objects.all()})


def project_detail(request, pk):
    return render(request, 'project_detail.html', {'project': get_object_or_404(Project, pk=pk)})
