from multiprocessing import context
from django.shortcuts import render
from .models import Todo, Category

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'index.html', context)