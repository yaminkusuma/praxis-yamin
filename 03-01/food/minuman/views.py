from django.shortcuts import render, redirect
from . import models

# Create your views here.
def index(req):
    if req.POST:
        models.minuman.objects.create(
            jenis= req.POST['jenis'],
            nama= req.POST['nama'],
            harga= req.POST['harga'],
        )
        return redirect('/minuman')
    koplak= models.minuman.objects.all()
    return render(req, 'minum/index.html', {
        'data_minum' : koplak,
    })

def hapusMinuman(req, id):
    models.minuman.objects.filter(pk=id).delete()
    return redirect('/minuman/')