from django.db import models


class AbstractModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        abstract = True


class Task(AbstractModel):
    summary = models.CharField(max_length=50, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    type = models.ForeignKey('webapp.Type', related_name='tasks', on_delete=models.PROTECT, verbose_name='Тип', null=True)
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.PROTECT, verbose_name='Статус', null=True)

    def __str__(self):
        return f"Task {self.summary}"


class Type(AbstractModel):
   title = models.CharField(max_length=40, verbose_name='Название')

   def __str__(self):
       return self.title


class Status(AbstractModel):
    title = models.CharField(max_length=40, verbose_name='Название')

    def __str__(self):
        return self.title
