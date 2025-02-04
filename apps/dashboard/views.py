from django.shortcuts import render, redirect

def dashboard_page(request):
    return render(request, "dashboard/dashboard.html")

def settings(request):
    return render(request, "dashboard/settings.html")