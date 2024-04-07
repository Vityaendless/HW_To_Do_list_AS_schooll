from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, TemplateView, FormView
from ..models import Task
from ..forms import TaskForm

from django.db.models import Q, F
from datetime import datetime, timedelta


class IndexView(TemplateView):
    template_name = 'tasks/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        #1
        #context['tasks'] = Task.objects.filter(updated_at__date__gte=datetime.now().date() - timedelta(days=30), status__title__iexact='done')
        #2
        #context['tasks'] = Task.objects.filter((Q(status__title='Done') | Q(status__title='New')) & (Q(types__title='Task') | Q(types__title='Bug')))
        #3
        #context['tasks'] = Task.objects.filter(Q(types__title='Bug') | Q(summary__contains='bug'))
        #4
        #context['tasks'] = Task.objects.values('pk','id', 'summary', 'status__title', 'types__title')
        #5
        #context['tasks'] = Task.objects.filter(summary=F('description'))
        #6
        #context['tasks'] = Task.objects.filter(types__title='Task').count()
        #context['tasks'] = Task.objects.filter(types__title='Bug').count()
        #context['tasks'] = Task.objects.filter(types__title='Enhancement').count()
        return context


class TaskView(TemplateView):
    template_name = 'tasks/task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context


class TaskCreateView(FormView):
    template_name = 'tasks/new_task.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)


class TaskUpdateView(FormView):
    template_name = 'tasks/update_task.html'
    form_class = TaskForm

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('task_view', pk=self.task.pk)


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'tasks/delete_task.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')