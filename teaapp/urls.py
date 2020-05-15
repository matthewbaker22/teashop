from django.urls import path
from .views import *
from teaapp import views

app_name = "teaapp"

urlpatterns = [
    path('', tea_list, name="tea_list"),
    path('tea/form', tea_form, name='tea_form'),
    path('teas/<int:tea_id>/', tea_details, name='tea_details'),
]
