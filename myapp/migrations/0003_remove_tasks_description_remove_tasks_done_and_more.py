# Generated by Django 4.2 on 2023-05-10 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_tasks_delete_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasks',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='done',
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='project',
        ),
    ]