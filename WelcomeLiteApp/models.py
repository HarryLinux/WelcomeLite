from django.db import models

class JobTitle(models.Model):
    job_title = models.CharField(max_length=64)

    def __str__(self):
        return self.job_title

class JobOffer(models.Model):
    candidate_first_name = models.CharField(max_length=64)
    candidate_last_name = models.CharField(max_length=64)
    candidate_email = models.EmailField(max_length=256)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    offer_amount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.candidate_first_name + ' ' + self.candidate_last_name
