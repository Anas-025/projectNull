from django.urls import path

from . import views

urlpatterns = [
    path("public/transform" , views.transform, name="transform"),
]