from django.db import models
import uuid

# Create your models here.
class Task(models.Model):
    CHOICES = [('C','Completed'),('F','In Progress')]

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    status = models.CharField(choices=CHOICES, max_length=128)

    def __str__(self):
        return self.name

class Timer(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()