# Generated by Django 5.0.2 on 2024-05-19 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_project_users_alter_project_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('update_users_in_project', 'Can update users in project')]},
        ),
    ]