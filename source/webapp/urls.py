from django.urls import path
from .views import IndexView, TaskView, TaskCreateView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('articles/add/', TaskCreateView.as_view(), name='new_task'),
]
