from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('task-list/', views.taskList, name='task-list'),
]