
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"), 
    path('upload_form', views.modify_values_ftn, name = "modif_values")    
]