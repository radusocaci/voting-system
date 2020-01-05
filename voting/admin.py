from django.contrib import admin

from .models import Candidate, VotingSession, VoteUser

# Register your models here.
admin.site.register(Candidate)
admin.site.register(VotingSession)
admin.site.register(VoteUser)
