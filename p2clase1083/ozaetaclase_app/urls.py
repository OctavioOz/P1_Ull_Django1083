from django.urls import path
from . import views

urlpatterns = [
    path("",views.hola,name="ozaetaclase_app")
]
