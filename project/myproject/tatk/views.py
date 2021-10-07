from django.shortcuts import render, redirect

# Create your views here.
from . import models
def index(request):
    if request.POST:
        models.Kodok.objects.create(name=request.POST['name'])
        return redirect("/")
    tasks = models.Kodok.objects.all()
    return render (request, "index.html",{
        "data": tasks
    })

