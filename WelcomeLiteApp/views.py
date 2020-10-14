from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse

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
    # if job offer does not exist, return to index with error message
    # else, delete job offer and return to index
    try:
        job_offer = JobOffer.objects.get(pk=job_offer_id)
    except (KeyError, JobOffer.DoesNotExist):
        # Return to job offer list
        return render(request, 'WelcomeLiteApp/index.html', {
            'error_message': 'Job offer does not exist.'
        })
    else:
        candiate_name = str(job_offer)
        job_offer.delete()
        return HttpResponseRedirect(reverse('welcome:index'))
