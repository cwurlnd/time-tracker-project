from django.urls import path

from . import views

urlpatterns = [
    path('create', views.PostTaskView.as_view(), name='create'),
    path('', views.ReadTaskView.as_view(), name='read'),
    path('<int:pk>/update/', views.UpdateTaskView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete'),
    path('task_dash/<int:week>/<int:month>/', views.TaskDash.as_view(), name='task dashboard'),
    path('time_dash/<int:week>/<int:month>/', views.TimeDash.as_view(), name='time dashboard'),
    path('timer_create/', views.PostTimerView.as_view(), name='timer create'),
    path('timer_list/', views.ReadTimerView.as_view(), name='timer list'),
    path('<int:pk>/timer/update/', views.UpdateTimerView.as_view(), name='timer update'),
    path('<int:pk>/timer/delete/', views.DeleteTimerView.as_view(), name='timer delete'),
]
