# Generated by Django 5.0.3 on 2024-03-17 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='task',
        ),
        migrations.RemoveField(
            model_name='type',
            name='task',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.status', verbose_name='Статус'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.type', verbose_name='Тип'),
            preserve_default=False,
        ),
    ]
