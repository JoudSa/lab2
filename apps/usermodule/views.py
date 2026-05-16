from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           raw_password = form.cleaned_data.get('password1')
           user.set_password(raw_password)
           user.save()
           messages.success(request, 'You have successfully registered!')
           return redirect('login')
        else:
            messages.error(request, 'Error during registration. Please check the form.')
    else:
        form = SignUpForm()
        
    return render(request, "usermodule/register.html",{"form":form})

def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) 
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('lab11_list_students')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    
    return render(request, "usermodule/login.html", {"form": form})

def logoutUser(request):
    logout(request)
    return redirect('login')
        
        