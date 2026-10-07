from django.urls import path
from . import views

app_name = 'home_Jessica_Marian'

urlpatterns = [
    path('', views.base, name='base'),
]