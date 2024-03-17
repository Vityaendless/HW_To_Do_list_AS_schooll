# Generated by Django 5.0.3 on 2024-03-17 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_task_status_alter_task_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.status', verbose_name='Статус'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.type', verbose_name='Тип'),
            preserve_default=False,
        ),
    ]
