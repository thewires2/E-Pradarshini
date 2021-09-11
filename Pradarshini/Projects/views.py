from django.shortcuts import render
from .models import ProjectModel

# Create your views here.

def project_main(request, *args, **kwargs):
    return render(request, 'Projects/project.html',{
        "Data": ProjectModel.objects.all()
    })

def project_details(request,pk):
    return render(request, 'Projects/project_details.html',{
        "Data": ProjectModel.objects.get(pk=pk)
    })