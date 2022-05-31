from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_add, name='todo'),
    path('delete/<int:id>/', views.delete, name='delete'),
]