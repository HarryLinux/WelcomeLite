from django.db import models

class JobOffer(models.Model):
    candidate_first_name = models.CharField(max_length=64)
    candidate_last_name = models.CharField(max_length=64)
    candidate_email = models.EmailField(max_length=254)
    offer_amount = models.PositiveIntegerField(default=0)