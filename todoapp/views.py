from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category, Todo
from .forms import AddForm, AsignTodoForm


def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username= request.POST.get('username').lower()
        password= request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username or password doesnt exist')
    context = {'page': page}
    return render(request, 'todoapp/login-register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = UserCreationForm()
    context = {'form': form}

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')
    return render(request, 'todoapp/login-register.html', context)

def home(request):
    todos = Todo.objects.all()
    categories = Category.objects.all()
    q = request.GET.get('q')
    if q :
        todos = Todo.objects.filter(
            Q(name__icontains = q) |
            Q(category__type__icontains = q)
        )
    context = {'todos': todos, 'categories':categories}
    return render(request, 'todoapp/index.html', context)

def about(request):
    return render(request, 'todoapp/about.html')

def add_todo(request):
    page = 'add-todo'
    form  = AddForm()
    context = {'form': form, 'page': page}
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
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'todoapp/add.html', context)

def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('home')
    return render(request, 'todoapp/delete.html', {'obj': todo})

def assignTodo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = AsignTodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {'form': form}
    return render(request, 'todoapp/add.html', context)

