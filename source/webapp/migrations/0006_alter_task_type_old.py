# Generated by Django 5.0.3 on 2024-03-20 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_type_task_type_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='type_old',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tasks_old', to='webapp.type', verbose_name='Тип'),
        ),
    ]