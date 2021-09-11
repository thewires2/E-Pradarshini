from django.shortcuts import render
from .models import ProjectModel
from .forms import ProjectForm


# Create your views here.

def project_main(request, *args, **kwargs):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            return render(request, 'Projects/project.html',{
        "Data": ProjectModel.objects.all(),
        "form": form,
    })
    else:
        form = ProjectForm()
    return render(request, 'Projects/project.html',{
        "Data": ProjectModel.objects.all(),
        "form": form,
    })

def project_details(request,pk):
    return render(request, 'Projects/project_details.html',{
        "Data": ProjectModel.objects.get(pk=pk),
        
    })