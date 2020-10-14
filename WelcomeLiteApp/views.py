# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import JobOffer

def index(request):
    job_offer_list = JobOffer.objects.all()
    template = loader.get_template('WelcomeLiteApp/index.html')
    context = { 'job_offer_list': job_offer_list }
    return HttpResponse(template.render(context, request))

def add_offer(request):
    return HttpResponse("We made it to the add offers page!")

def edit_offer(request):
    return HttpResponse("Another page for editing offers")