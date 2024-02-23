from django.urls import path
from .views import index, new, view, delete, update


urlpatterns = [
    path('', index, name='index'),
    path('new_task/', new, name='new_task'),
    path('task/<int:pk>/', view, name='view'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('update/<int:pk>/', update, name='update'),
]
