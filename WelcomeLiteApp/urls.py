from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addOffer/', views.add_offer, name='add'),
    path('editOffer/<int:job_offer_id>/', views.edit_offer, name='edit'),
    path('deleteOffer/<int:job_offer_id>/', views.delete_offer, name='delete')
]