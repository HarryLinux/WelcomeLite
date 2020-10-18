from django.urls import path

from . import views

app_name = 'welcome'
urlpatterns = [
    path('', views.index, name='index'), # shows job offer list
    path('addOffer/', views.add_offer, name='add'), # handles get and post requests for insert operations
    path('editOffer/<int:job_offer_id>/', views.add_offer, name='edit'), # handles get and post requests for update operations 
    path('deleteOffer/<int:job_offer_id>/', views.delete_offer, name='delete') # handles deletions
]