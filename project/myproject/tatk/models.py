from django.db import models
# Create your models here.

class Kodok(models.Model):
    name = models.TextField(default='')