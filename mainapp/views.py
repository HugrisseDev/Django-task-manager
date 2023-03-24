from django.shortcuts import render, redirect

from .forms import CreateUserForm, Loginform, CreateTaskForm
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Task




# Create your views here.
@login_required(login_url="/login")
def home(request):
    
    return render(request, 'home.html')

# -------------- Registration User --------------

def register(request):
    
    form = CreateUserForm
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
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
                return redirect("home")
            
    context = {'form': form}
    return render(request, 'login.html', context = context)


# -------------- Logout User --------------

def logout(request):
    
    auth.logout(request)
    
    return redirect("home")


# -------------- User Dashboard --------------
@login_required(login_url='login')
def dashboard(request):
    
    return render(request, 'profile/dashboard.html')


# -------------- Create Task --------------
@login_required(login_url='login')
def createtask(request):
    
    form = CreateTaskForm()
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')
    
    context = {'form' : form}
    return render(request, 'profile/createtask.html', context=context)



# -------------- View Task --------------
@login_required(login_url='login')
def viewtask(request):
    
    curr_user = request.user.id
    
    task = Task.objects.all().filter(user=curr_user)
    
    context = {'task': task}
    return render(request, 'profile/viewtask.html', context = context)


# -------------- update Task --------------
@login_required(login_url='login')
def updatetask(request, pk):
    task = Task.objects.get(id = pk)
    form = CreateTaskForm(instance = task)
    
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save()
            return redirect('viewtask')
        
    context = {'form':form}
    return render(request, 'profile/updatetask.html', context = context )
    
    
    
# -------------- Delete Task -------------- -
@login_required(login_url='login')
def deletetask(request, pk):
    task = Task.objects.get(id = pk)
    if request.method == 'POST':
        task.delete()
        return redirect('viewtask')
    
    return render(request, 'profile/deletetask.html')   


# -------------- Delete Account ---------------

@login_required(login_url='login')
def deleteaccount(request):
    
    if request.method == 'POST':
        deleteUser = User.objects.get(username = request.user)
        deleteUser.delete()
        redirect('home')
        
    return render(request, 'profile/deleteaccount.html')

  
 
        

