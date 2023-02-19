from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse 


# Create your views here.

def home(request):
    
    taksList = Task.objects.all()
    
    context = {'tasks' : taksList}
    
    return render(request, 'home.html', context = context)


def about(request):
    return render(request, template_name='about.html')

def createTask(request):
    form = TaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request,'taskForm.html', context = context)

def updateTask(request, pk):
    
    task = Task.objects.get(id=pk)
    
    form = TaskForm(instance=task)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request,'taskForm.html', context)


