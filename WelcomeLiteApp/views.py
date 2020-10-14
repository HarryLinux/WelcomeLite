from django.http import HttpResponse
from django.shortcuts import render

from .models import JobOffer

def index(request):
    job_offer_list = JobOffer.objects.all()
    context = { 'job_offer_list': job_offer_list }
    return render(request, 'WelcomeLiteApp/index.html', context)

def add_offer(request):
    return HttpResponse("We made it to the add offers page!")

def edit_offer(request, job_offer_id):
    return HttpResponse("You're editing offer %s" % job_offer_id)

def delete_offer(request, job_offer_id):
    return HttpResponse("You're deleting offer %s" % job_offer_id)