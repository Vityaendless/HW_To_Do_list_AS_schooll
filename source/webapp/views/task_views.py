from django.shortcuts import get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from ..models import Task, Project
from ..forms import TaskForm


class TaskView(DetailView):
    model = Task
    template_name = 'tasks/task_view.html'


class TaskCreateView(CreateView):
    template_name = 'tasks/new_task.html'
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect('project', pk=project.pk)


class TaskUpdateView(UpdateView):
    template_name = 'tasks/update_task.html'
    model = Task
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    template_name = 'tasks/delete_task.html'
    model = Task

    def get_success_url(self):
        return reverse('project', kwargs={'pk': self.object.project.pk})