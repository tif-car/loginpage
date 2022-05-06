from django.urls import path      
from . import views   

urlpatterns = [
    path('todolist', views.todoappView, name= 'todolist'),
    path('todolist', views.todo, name = 'todo'),
    path('addTodoItem', views.addTodoView, name = 'addToDo'),
]


