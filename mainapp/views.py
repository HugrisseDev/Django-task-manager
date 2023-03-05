from django.shortcuts import render, redirect

from .forms import CreateUserForm, Loginform
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required




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
                return redirect("home")
            
    context = {'form': form}
    return render(request, 'login.html', context = context)


# -------------- Logout User --------------

def logout(request):
    
    auth.logout(request)
    
    return redirect("home")

# -------------- User Dashboard --------------

def dashboard(request):
    
    return render(request, 'profile/dashboard.html')




# Views must be secured..