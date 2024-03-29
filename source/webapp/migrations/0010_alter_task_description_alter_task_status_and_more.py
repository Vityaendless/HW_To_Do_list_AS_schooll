# Generated by Django 5.0.2 on 2024-03-29 15:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_remove_task_type_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=3000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.status', verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='task',
            name='types',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='webapp.type', verbose_name='Types'),
        ),
    ]
