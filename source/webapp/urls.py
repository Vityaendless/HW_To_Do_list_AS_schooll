from django.urls import path
from .views import IndexView, TaskView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('tasks/add/', TaskCreateView.as_view(), name='new_task'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
]
