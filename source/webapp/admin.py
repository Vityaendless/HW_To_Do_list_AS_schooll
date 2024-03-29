from django.contrib import admin
from .models import Task, Type, Status


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'created_at']
    list_display_links = ['id', 'summary']
    list_filter = ['summary', 'description', 'created_at']
    search_fields = ['summary', 'description']
    fields = ['summary', 'description', 'types', 'status', 'created_at', 'updated_at']
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
