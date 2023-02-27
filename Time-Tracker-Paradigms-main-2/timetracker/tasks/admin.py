from django.contrib import admin
from .models import Task, Timer

# Register your models here.
admin.site.register(Task)
admin.site.register(Timer)