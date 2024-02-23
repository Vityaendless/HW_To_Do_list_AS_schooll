from django.shortcuts import render, redirect, get_object_or_404
from django.http import  HttpResponseRedirect
from .models import Task, status_choices


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def new(request):
    if request.method == 'GET':
        return render(request, 'new_task.html', {'statuses': status_choices})
    elif request.method == 'POST':
        task = Task.objects.create(
            description=request.POST.get('description'),
            full_description=request.POST.get('full_description'),
            status=request.POST.get('status'),
            deadline=request.POST.get('deadline')
        )
        return redirect('view', pk=task.pk)


def view(request, *args, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'view.html', {'task': task})


def delete(request, *args, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_delete.html', {'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('index')