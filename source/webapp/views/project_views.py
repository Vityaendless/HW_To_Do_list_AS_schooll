from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group
from ..models import Project
from ..forms import SimpleSearchForm, ProjectForm, UsersInProjectForm


class ProjectsView(ListView):
    model = Project
    template_name = 'projects/index.html'
    context_object_name = 'projects'
    paginate_by = 5
    paginate_orphans = 1
    ordering = ('-created_at',)

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']
        return None

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(title__icontains=self.search_value) |
                Q(description__icontains=self.search_value)
            )
        queryset = queryset.filter(is_deleted=False)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.search_form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search_value'] = self.search_value
        return context


class ProjectView(DetailView):
    model = Project
    template_name = 'projects/project_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.filter(is_deleted=False)
        return context


class ProjectCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'projects/new_project.html'
    model = Project
    form_class = ProjectForm
    permission_required = 'webapp.add_project'

    def form_valid(self, form):
        project = form.save(commit=False)
        project.save()
        project.users.set((self.request.user, ))
        form.save_m2m()
        return redirect('webapp:project', pk=project.pk)


class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'projects/update_project.html'
    model = Project
    form_class = ProjectForm
    permission_required = 'webapp.change_project'


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'projects/delete_project.html'
    model = Project
    permission_required = 'webapp.delete_project'

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get('pk'))
        project.is_deleted = True
        project.save()
        return redirect('webapp:index')


class UsersInProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'projects/update_users_in_project.html'
    model = Project
    form_class = UsersInProjectForm
    permission_required = 'webapp.change_project'

    def has_permission(self):
        developer = Group.objects.get_or_create(name='Developer')
        print(developer)
        no_access = len(self.request.user.groups.all()) == 1 and self.request.user.groups.first() == developer[0]
        return self.request.user in self.get_object().users.all() and not no_access
