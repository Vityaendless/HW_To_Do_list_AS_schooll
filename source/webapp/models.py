from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator


class AbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Time of create", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Time of update")

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
        return reverse('webapp:task_view', kwargs={'pk': self.pk})


class Type(AbstractModel):
   title = models.CharField(max_length=40, verbose_name='Type')

   def __str__(self):
       return self.title


class Status(AbstractModel):
    title = models.CharField(max_length=40, verbose_name='Status')

    def __str__(self):
        return self.title


class Project(AbstractModel):
    start_date = models.DateField(verbose_name="Start Date")
    end_date = models.DateField(verbose_name="End Date", null=True, blank=True)
    title = models.CharField(max_length=50, validators=[MinLengthValidator(5)], verbose_name="Title")
    users = models.ManyToManyField('auth.User', related_name='users', verbose_name='Users')
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Description")
    is_deleted = models.BooleanField(default=False, verbose_name='Deleted?')

    def __str__(self):
        return f"Project {self.title}"

    def get_absolute_url(self):
        return reverse('webapp:project', kwargs={'pk': self.pk})
