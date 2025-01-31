from django.shortcuts import render, redirect

def SignIn(request):
    return render(request, "signin.html")

def SignUp(request):
    return render(request, "signup.html")