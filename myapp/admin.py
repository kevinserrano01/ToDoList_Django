from django.contrib import admin
from myapp.models import Project, Tasks

class ProjectAdmin(admin.ModelAdmin):
    model = Project
    # Funciones
    list_display = ('id', 'name')

class TaskAdmin(admin.ModelAdmin):
    model = Tasks

    # Funciones
    list_display = ('id', 'title')

# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tasks, TaskAdmin)