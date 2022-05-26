from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Todo
from .forms import AddForm

# Create your views here.
def home(request):
    todos = Todo.objects.all()
    q = request.GET.get('q')
    if q :
        todos = Todo.objects.filter(
            Q(name__icontains = q) |
            Q(category__type__icontains = q)
        )
    context = {'todos': todos}
    return render(request, 'todoapp/index.html', context)

def about(request):
    return render(request, 'todoapp/about.html')

def add_todo(request):
    form  = AddForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'todoapp/add.html', context)

def view_todo(request,pk):
    todo = Todo.objects.get(id=pk)
    context = {'todo': todo}
    return render(request, 'todoapp/single_todo.html', context)

def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = AddForm(instance=todo)
    context= {'form': form}
    return render(request, 'todoapp/add.html', context)

def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'todoapp/delete.html', {'obj': todo})



