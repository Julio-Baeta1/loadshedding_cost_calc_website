from django.urls import path

from . import views

app_name = "loadshedding"

urlpatterns = [
    #path("", views.IndexView.as_view(), name="index"),
    path("", views.home, name="home"),
]