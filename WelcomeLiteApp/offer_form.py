from django import forms

from .models import JobOffer 

class JobOfferForm(forms.ModelForm):
    # Form model for a JobOffer object
    class Meta:
        model = JobOffer
        fields = ('candidate_first_name', 'candidate_last_name', 'candidate_email', 'job_title', 'offer_amount')
        
        # Set form labels
        labels = {
            'candidate_first_name': 'Candidate First Name',
            'candidate_last_name': 'Candidate Last Name',
            'candidate_email': 'Candidate Email Address',
            'job_title': 'Job Title',
            'offer_amount': 'Offer Amount'
        }

    def __init__(self, *args, **kwargs):
        super(JobOfferForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].empty_label = 'Select'
    