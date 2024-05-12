from django.contrib import admin
from .models import Task, Type, Status, Project


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'created_at']
    list_display_links = ['id', 'summary']
    list_filter = ['summary', 'description', 'created_at']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'types', 'status', 'project', 'is_deleted', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    list_filter = ['title']
    search_fields = ['title']
    fields = ['title']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    list_filter = ['title']
    search_fields = ['title']
    fields = ['title']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['title', 'users', 'description', 'created_at']
    search_fields = ['title', 'description', 'start_date', 'end_date']
    fields = ['title', 'description', 'users', 'start_date', 'end_date', 'is_deleted', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
