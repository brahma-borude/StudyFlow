from django.shortcuts import render, redirect

def SignIn(request):
    return render(request, "users/signin.html")

def SignUp(request):
    return render(request, "users/signup.html")