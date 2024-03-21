from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from .models import Task
from .forms import TaskForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context


class TaskCreateView(View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, 'new_task.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            task = Task.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status')
            )
            task.types.set(types)
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'new_task.html', {'form': form})


class TaskUpdateView(TemplateView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'types': task.types.all(),
            'status': task.status
        })
        return render(request, 'update_task.html', {'form': form})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            task.summary=form.cleaned_data.get('summary')
            task.description=form.cleaned_data.get('description')
            #task.types=form.cleaned_data.get('types')
            task.status = form.cleaned_data.get('status')
            task.types.set(types)
            task.save()
            return redirect('task_view', pk=task.pk)
        else:
            return render(request, 'update_task.html', {'form': form})


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'delete_task.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')