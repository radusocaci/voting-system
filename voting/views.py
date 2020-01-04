from django.shortcuts import render, get_object_or_404
from voting.models import Candidate, VotingSession


def dashboard(request):
    return render(request, 'dashboard.html', {'dashboard': VotingSession.objects.all()})


def votedash(request, pk):
    return render(request, 'votedash.html', {'voting': get_object_or_404(VotingSession, pk=pk)})


def about_page(request):
    return render(request, 'about.html', {})
