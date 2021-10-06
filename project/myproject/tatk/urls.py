from django.shortcuts import render
from django.urls import path

from . import views
def index(req):
    return render(req, 'index.html')

urlpatterns = [
    path('', index)
]
