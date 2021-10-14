from django.shortcuts import redirect, render
from . import models

# Create your views here.

def index(req):
    if req.POST:
        models.makanan.objects.create(
            jenis= req.POST['jenis'],
            nama= req.POST['nama'],
            harga= req.POST['harga'],
        )
        return redirect('/makanan')
    koplak= models.makanan.objects.all()
    return render(req, 'makan/index.html', {
        'data_makan' : koplak,
    })
    # return render(req, 'makan/index.html')

# def input_makan (req):