from django.db import models
from django.conf import settings  # Import settings to access AUTH_USER_MODEL

class Election(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    votes = models.IntegerField(default=0)

class Vote(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use settings.AUTH_USER_MODEL
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
