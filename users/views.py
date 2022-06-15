
from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from mycontacts import settings 

def signup(request):
    form = CustomUserCreationForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            messages.success(request,'Account created successfully')
           
            

    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def login_user(request):
    messages = ''
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
          login(request,user)
          
          return redirect ("index")
         

        else:
            messages ="Entrez de bon identifiants"
           
       

    return render(request,"users/login.html",{"message":messages})        

def logout_user(request):
    logout(request)
    return redirect("login")


        
