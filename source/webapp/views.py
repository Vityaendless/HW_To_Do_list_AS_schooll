from django.shortcuts import render
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
        Task.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            deadline=request.POST.get('deadline')
        )
        return HttpResponseRedirect('/')


def view(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(id=task_id)
    return render(request, 'view.html', {'task': task})


def delete(request):
    task_id = request.GET.get('id')
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect('/')