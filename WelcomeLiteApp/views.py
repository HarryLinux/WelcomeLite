from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse

from .models import JobOffer
from .offer_form import JobOfferForm

# GET request, displays list of Job Offers currently in DB
def index(request):
    job_offer_list = get_list_or_404(JobOffer)
    context = { 'job_offer_list': job_offer_list }
    return render(request, 'WelcomeLiteApp/index.html', context)

# GET and POST requests to Add & Edit offers
def add_offer(request, job_offer_id=0):
    if request.method == 'GET':
        # if id is 0 then we're doing insert operation
        # else update with JobOfferForm(instance=job_offer)
        if job_offer_id == 0:
            form = JobOfferForm()
        else: # GET JobOffer instance and populate data into JobOfferForm 
            job_offer = get_object_or_404(JobOffer, pk=job_offer_id)
            form = JobOfferForm(instance=job_offer)
        return render(request, 'WelcomeLiteApp/add_offer.html', { 'form': form })
    elif request.method == 'POST':
        if job_offer_id == 0: # Insert operation
            form = JobOfferForm(request.POST)
        else: # Update operation
            job_offer = get_object_or_404(JobOffer, pk=job_offer_id)
            form = JobOfferForm(request.POST, instance=job_offer)
        # check if form data is valid before saving and then redirect to index
        if form.is_valid():
            form.save()
        return redirect('/')

def delete_offer(request, job_offer_id):
    # if job offer does not exist, return to index with error message
    # else, delete job offer and return to index with success message
    try:
        job_offer = JobOffer.objects.get(pk=job_offer_id)
    except (KeyError, JobOffer.DoesNotExist):
        # Return to job offer list with error message
        job_offer_list = get_list_or_404(JobOffer)
        context = { 
            'job_offer_list': job_offer_list,
            'error_message': 'That job offer does not exist.'
            }
        return render(request, 'WelcomeLiteApp/index.html', context)
    else:
        # Return to job offer list with success message
        candidate_name = str(job_offer)
        job_offer_list = get_list_or_404(JobOffer)
        context = { 
            'job_offer_list': job_offer_list,
            'success_message': f"Successfully deleted {candidate_name}'s offer"
        }
        job_offer.delete()
        return render(request, 'WelcomeLiteApp/index.html', context)
