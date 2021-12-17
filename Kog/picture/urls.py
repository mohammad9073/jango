from django.urls import path
from . import views

urlpatterns = [
    path('dulce/' , views.dulce),
]