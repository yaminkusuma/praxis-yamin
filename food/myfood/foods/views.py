from django.shortcuts import redirect, render

from foods import models

# Create your views here.

def index(request):
    if request.POST:
        models.makanan.objects.create(
            nama = request.POST['nama'],
            jenis = request.POST['jenis'],
            harga = request.POST['harga'],
        )
        return redirect('/')
    makan1 = models.makanan.objects.all()
    return render(request, 'index.html', {
        'makanan': makan1,
    })

# def index(request):
#     if request.POST:
#         models.minuman.objects.create(
#             nama = request.POST['nama'],
#             jenis = request.POST['jenis'],
#             harga = request.POST['harga'],
#         )
#         return redirect('/')
#     makan1 = models.makanan.objects.all()
#     return render(request, 'index.html', {
#         'makanan': makan1,
#     })
# def input(request):
