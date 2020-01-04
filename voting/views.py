from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from voting.models import VotingSession, VoteUser, Candidate


def dashboard(request):
    return render(request, 'dashboard.html', {'dashboard': VotingSession.objects.filter(active=True)})


@login_required
def votedash(request, pk):
    return render(request, 'votedash.html', {'voting': get_object_or_404(VotingSession, pk=pk)})


def about_page(request):
    return render(request, 'about.html', {})


def vote(request, candidate_id, voting_session_id):
    if settings.GLOBAL_SETTINGS.get('default_image') in request.user.profile.image.path:
        return redirect('profile')
    else:
        candidate = Candidate.objects.gecht(pk=candidate_id)
        voting_session = VotingSession.objects.get(pk=voting_session_id)
        rows = VoteUser.objects.filter(voting_session=voting_session, user=request.user)

        if rows.count() == 0:
            user_vote = VoteUser(candidate=candidate, voting_session=voting_session, user=request.user)
            user_vote.save()
            messages.success(request, f'Your vote has been registered successfully!')
        else:
            messages.warning(request, f'Your already voted in this election!')

        return redirect(reverse('votedash', kwargs={'pk': voting_session_id}))
