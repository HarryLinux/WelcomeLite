from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addOffer/', views.add_offer, name='add'),
    path('editOffer/', views.edit_offer, name='add')
]