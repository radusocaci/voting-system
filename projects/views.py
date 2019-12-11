from django.shortcuts import render

from projects.models import Project


# Create your views here.


def projects_index(request):
    return render(request, 'projects_index.html', {'projects': Project.objects.all()})


def project_detail(request, pk):
    return render(request, 'project_detail.html', {'projects': Project.objects.get(pk=pk)})
