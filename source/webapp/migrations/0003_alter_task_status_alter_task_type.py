# Generated by Django 5.0.3 on 2024-03-17 16:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_status_task_remove_type_task_task_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.status', verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.type', verbose_name='Тип'),
        ),
    ]