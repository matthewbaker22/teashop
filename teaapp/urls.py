from django.urls import path
from .views import *
from teaapp import views

app_name = "teaapp"

urlpatterns = [
    path('', tea_list, name="tea_list")
]
