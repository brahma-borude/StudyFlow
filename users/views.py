from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account {{username}}has been created!")
            return redirect("signin")
    else:
        form = UserRegisterForm()
    return render(request, "users/signup.html", {"form":form})

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, "Useranme or Password is incorrect")
    return render(request, "users/signin.html")

def logoutUser(request):
    logout(request)
    return redirect("signin")