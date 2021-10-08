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

def hapus (request, id):
    models.Kodok.objects.filter(pk = id).delete()
    return redirect('/')


# def edit(request):
    if request.POST:
        models.Kodok.objects.filter(name=request.POST['name'])
        return redirect("/")
    tasks = models.Kodok.objects.all()
    return render (request, "edit.html",{
        "data": tasks,
    })

def edit (request, id):
    models.Kodok.objects.filter(pk = id).update()
    return render(request, "edit.html")
    
 
# def detail(request.id):                                                                                                                                                                                                                                                                                                                                                                           