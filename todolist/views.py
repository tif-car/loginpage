from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .models import TodoListItem

# Create your views here.
def todo(request):
    return render(request, 'todolist.html')

def todoappView(request):
    all_todo_items = TodoListItem.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_todo_items})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todolist/') 