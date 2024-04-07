from django.urls import path
from .views import (IndexView, TaskView, TaskCreateView, TaskUpdateView, TaskDeleteView,
                    ProjectsView, ProjectView, ProjectCreateView, ProjectUpdateView,
                    ProjectDeleteView)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/add/', TaskCreateView.as_view(), name='new_task'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('project/<int:pk>', ProjectView.as_view(), name='project'),
    path('project/add/', ProjectCreateView.as_view(), name='new_project'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='update_project'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
]
