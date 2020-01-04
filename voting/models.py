from django.db.models import *
from django.db import models


# Create your models here.

class Candidate(Model):
    name = CharField(max_length=100)
    description = TextField()
    image = models.ImageField(upload_to='candidate_pics')


class VotingSession(Model):
    name = CharField(max_length=100)
    active = models.BooleanField(default=True)
    year = IntegerField()
    country = CharField(max_length=100)
    image = models.ImageField(upload_to='voting_pics')
    candidates = models.ManyToManyField('Candidate', related_name='candidates')
