from django.db import models

# Create your models here.
# Un modelo de Django es una tabla en su base de datos.

class Project(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Tasks(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title