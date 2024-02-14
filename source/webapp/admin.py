from django.contrib import admin
from .models import Task
# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'created_at']
    list_display_links = ['id', 'description']
    list_filter = ['created_at', 'status']
    search_fields = ['description']
    fields = ['description', 'status', 'deadline', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']