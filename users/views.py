from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created!")
            return redirect("dashboard")
    else:
        form = UserRegisterForm()
    return render(request, "users/signup.html", {"form":form})

def signin(request):
    return render(request, "users/signin.html")