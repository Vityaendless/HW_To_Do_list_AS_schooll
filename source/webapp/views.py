from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def new(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'new_task.html', {'form': form})
    elif request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                description=request.POST.get('description'),
                full_description=request.POST.get('full_description'),
                status=request.POST.get('status'),
                deadline=request.POST.get('deadline')
            )
            return redirect('view', pk=task.pk)
        else:
            return render(request, 'new_task.html', {'form': form})


def update(request, *args, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            'description': task.description,
            'full_description': task.full_description,
            'status': task.status,
            'deadline': task.deadline
        })
        return render(request, 'task_update.html', {'form': form})
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data.get('description')
            task.full_description = form.cleaned_data.get('full_description')
            task.status = form.cleaned_data.get('status')
            task.deadline = form.cleaned_data.get('deadline')
            task.save()
            return redirect('view', pk=task.pk)
        else:
            return render(request, 'task_update.html', {'form': form})


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