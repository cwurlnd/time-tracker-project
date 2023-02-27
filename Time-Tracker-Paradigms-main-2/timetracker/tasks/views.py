from django.shortcuts import render
import datetime

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Task, Timer

class PostTaskView(CreateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['name', 'description', 'project', 'status']
    success_url = "/"

class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = "/"

class UpdateTaskView(UpdateView):
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['name', 'description', 'project', 'status']
    success_url = "/"
    template_name_suffix = "_update_form"

class ReadTaskView(ListView):
    template_name = 'tasks/tasklist.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        """Return all tasks."""
        return Task.objects.all()

# timers
class PostTimerView(CreateView):
    model = Timer
    template_name = 'timers/timer_form.html'
    fields = ['task', 'start', 'end']
    success_url = "../timer_list"

class DeleteTimerView(DeleteView):
    model = Timer
    template_name = 'timers/delete.html'
    success_url = "../../../timer_list"

class UpdateTimerView(UpdateView):
    model = Timer
    template_name = 'timers/timer_form.html'
    fields = ['start', 'end']
    success_url = "../../../timer_list"
    template_name_suffix = "_update_form"

class ReadTimerView(ListView):
    template_name = 'timers/timerslist.html'
    context_object_name = 'timer_list'

    def get_queryset(self):
        """Return all tasks."""
        return Timer.objects.all()

class TaskDash(ListView):
    model = Timer
    template_name = 'tasks/task_dash.html'
    context_object_name = 'timer_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["week"] = self.kwargs['week']
        context["month"] = self.kwargs['month']

        weekly = {}
        monthly = {}
        weeklyCount = {}
        monthlyCount = {}

        for timer in Timer.objects.all():
            if (timer.start.isocalendar()[1] == self.kwargs['week']):
                difference = timer.end - timer.start
                duration_in_s = difference.total_seconds()
                weekly[timer.task] = weekly.get(timer.task, 0) + duration_in_s
                weeklyCount[timer.task] = weeklyCount.get(timer.task, 0) + 1
            if (timer.start.month == self.kwargs['month']):
                difference = timer.end - timer.start
                duration_in_s = difference.total_seconds()
                monthly[timer.task] = monthly.get(timer.task, 0) + duration_in_s
                monthlyCount[timer.task] = monthlyCount.get(timer.task, 0) + 1

        weeklyAvg = {}
        monthlyAvg = {}
        for key in weekly:
            weeklyAvg[key] = weekly[key] / weeklyCount[key]
        for key in monthly:
            monthlyAvg[key] = monthly[key] / monthlyCount[key]

        context["weeklyTask"] = weeklyAvg
        context["monthlyTask"] = monthlyAvg
        
        return context

class TimeDash(ListView):
    model = Timer
    template_name = 'timers/time_dash.html'
    context_object_name = 'timer_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["week"] = self.kwargs['week']
        context["month"] = self.kwargs['month']

        weekly = {}
        monthly = {}
        weeklyProject = {}
        monthlyProject = {}

        for timer in Timer.objects.all():
            if (timer.start.isocalendar()[1] == self.kwargs['week']):
                difference = timer.end - timer.start
                duration_in_s = difference.total_seconds()
                weekly[timer.task] = weekly.get(timer.task, 0) + duration_in_s
                weeklyProject[timer.task.project] = weeklyProject.get(timer.task.project, 0) + duration_in_s
            if (timer.start.month == self.kwargs['month']):
                difference = timer.end - timer.start
                duration_in_s = difference.total_seconds()
                monthly[timer.task] = monthly.get(timer.task, 0) + duration_in_s
                monthlyProject[timer.task.project] = monthlyProject.get(timer.task.project, 0) + duration_in_s

        context["weeklyTimers"] = weekly
        context["monthlyTimers"] = monthly
        context["weeklyProjectTimers"] = weeklyProject
        context["monthlyProjectTimers"] = monthlyProject
        return context