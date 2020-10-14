from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import JobOffer

def index(request):
    job_offer_list = get_list_or_404(JobOffer)
    context = { 'job_offer_list': job_offer_list }
    return render(request, 'WelcomeLiteApp/index.html', context)

def add_offer(request):
    return render(request, 'WelcomeLiteApp/add_offer.html')

def edit_offer(request, job_offer_id):
    job_offer = get_object_or_404(JobOffer, pk=job_offer_id)
    return render(request, 'WelcomeLiteApp/edit_offer.html', { 'job_offer': job_offer })

def delete_offer(request, job_offer_id):
    job_offer = get_object_or_404(JobOffer, pk=job_offer_id) 
    return HttpResponse("You're deleting offer %s" % job_offer_id)