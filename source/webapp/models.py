from django.db import models

# Create your models here.


status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    description = models.CharField(max_length=100, verbose_name='Описание')
    full_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Подробное описание")
    status = models.CharField(max_length=30, verbose_name='Статус', choices=status_choices)
    deadline = models.CharField(max_length=10, null=True, blank=True, verbose_name='Дата окончания')
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f"{self.id}, {self.description}"
