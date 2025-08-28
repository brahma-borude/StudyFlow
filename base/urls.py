from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("create-course/", views.create_course, name="create-course"),
]
