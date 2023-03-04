from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, CreateUserForm, Loginform
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login




# Create your views here.

def home(request):
    
    taksList = Task.objects.all()
    
    context = {'tasks' : taksList}
    
    return render(request, 'home.html', context = context)


def about(request):
    return render(request, template_name='about.html') 

# -------------- create task view --------------

def createTask(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request,'taskForm.html', context = context)

# -------------- update task view --------------

def updateTask(request, pk):
    
    task = Task.objects.get(id=pk)
    
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request,'taskForm.html', context = context)


# -------------- delete task view --------------

def deleteTask(request, pk):
    
    task = Task.objects.get(id = pk)
    
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    
    context = {'object': task}
    return render(request, 'delete.html', context)
    
# -------------- Registration User --------------

def register(request):
    
    form = CreateUserForm
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("welcome")
        
    context = {'form' : form}
    return render(request, 'register.html', context = context)

# -------------- Login User --------------

def login(request):
    form = Loginform
    
    if request.method == 'POST':
        form = Loginform(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            
    context = {'form': form}
    return render(request, 'login.html', context = context)


def logout(request):
    
    auth.logout(request)
    
    return redirect("home")


def dashboard(request):
    
    return render(request, 'dashboard.html')




# Views must be secured..