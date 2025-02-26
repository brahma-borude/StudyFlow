from django.shortcuts import render, redirect
from .forms import SignUpUserForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Sign Up page
def SignUp(request):
    if request.method == 'POST':
        form = SignUpUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            messages.success(request, "Account created successfully")
            return redirect("dashboard", {"form":form})
    else:
        form = SignUpUserForm()
    return render(request, "users/signup.html", {"form": form})

# Sign In page
def SignIn(request):
    return render(request, "users/signin.html")
