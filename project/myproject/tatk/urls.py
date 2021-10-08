from django.urls import path

from . import views
urlpatterns = [
    path('', views.index),
    path('<id>/hapus', views.hapus),
    # path('<id>/rincian', views.rincian),
    path('<id>/edit', views.edit),
    
]
