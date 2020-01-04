from django.contrib import admin
from .models import Candidate, VotingSession

admin.site.register(Candidate)
admin.site.register(VotingSession)
# Register your models here.
