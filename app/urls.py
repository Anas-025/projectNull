from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/util/v1/" , include("app.api.v1.urls")),
]