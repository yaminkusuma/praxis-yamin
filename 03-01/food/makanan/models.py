from django.db import models

# Create your models here.
class makanan(models.Model):
    jenis =  models.TextField(max_length=200)
    nama = models.TextField(default="")
    harga = models.IntegerField(default=0)