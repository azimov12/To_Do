from django.urls import path
from .views import CreateToDo, DeleteToDo, UpdateToDo, All

urlpatterns = [
    path('all/', All.as_view()),
    path('create/',CreateToDo.as_view()),
    path('update/<int:task_id>', UpdateToDo.as_view()),
    path('delete/<int:task_id>', DeleteToDo.as_view()),
]