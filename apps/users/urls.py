from django.urls import path
from . import views

urlpatterns = [
    path("", views.SignIn, name="signin"),
    path("signup/", views.SignUp, name="signup"),
]
