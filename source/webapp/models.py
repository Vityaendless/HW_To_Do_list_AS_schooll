from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator


class AbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        abstract = True


class Task(AbstractModel):
    summary = models.CharField(max_length=50, validators=[MinLengthValidator(5)], verbose_name="Summary")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")
    #type_old = models.ForeignKey('webapp.Type', related_name='tasks_old', on_delete=models.PROTECT, verbose_name='Тип')
    types = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Types')
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.PROTECT, verbose_name='Status')
    project = models.ForeignKey('webapp.Project', related_name='tasks', on_delete=models.PROTECT, verbose_name='Project')
    is_deleted = models.BooleanField(default=False, verbose_name='Deleted?')

    def __str__(self):
        return f"Task {self.summary}"

    def get_absolute_url(self):
        return reverse('task_view', kwargs={'pk': self.pk})


class Type(AbstractModel):
   title = models.CharField(max_length=40, verbose_name='Название')

   def __str__(self):
       return self.title


class Status(AbstractModel):
    title = models.CharField(max_length=40, verbose_name='Название')

    def __str__(self):
        return self.title


class Project(AbstractModel):
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date", null=True, blank=True)
    title = models.CharField(max_length=50, validators=[MinLengthValidator(5)], verbose_name="Title")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")
    is_deleted = models.BooleanField(default=False, verbose_name='Deleted?')

    def __str__(self):
        return f"Task {self.title}"

    def get_absolute_url(self):
        return reverse('project', kwargs={'pk': self.pk})
