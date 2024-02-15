from django.urls import path
from .views import index, new, view, delete

urlpatterns = [
    path('', index),
    path('new_task/', new),
    path('task/<int:pk>/', view),
    path('delete/<int:pk>/', delete),
]