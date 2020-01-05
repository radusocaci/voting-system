from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from voting.models import VotingSession, VoteUser, Candidate
from .forms import ContactForm


def dashboard(request):
    return render(request, 'dashboard.html', {'dashboard': VotingSession.objects.filter(active=True)})


def results_dashboard(request):
    return render(request, 'results.html', {
        'active_sessions': VotingSession.objects.filter(active=True),
        'inactive_sessions': VotingSession.objects.filter(active=False)
    })


@login_required
def votedash(request, pk):
    return render(request, 'votedash.html', {'voting': get_object_or_404(VotingSession, pk=pk)})


def results_detail(request, pk):
    voting_session = get_object_or_404(VotingSession, pk=pk)
    labels, data = generate_statistics_and_context(voting_session)
    labels_chart, data_chart = str(labels).replace("'", '"'), str(data).replace("'", '"')

    return render(request, 'results_detail.html', {
        'voting_session': voting_session,
        'labels': labels,
        'data': data,
        'labels_chart': labels_chart,
        'data_chart': data_chart
    })


def about_page(request):
    return render(request, 'about.html', {})


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('Support Request', message, sender_email, [settings.EMAIL_HOST_USER])

            messages.success(request, f'The message has been sent! We will contact you shortly.')

            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def vote(request, candidate_id, voting_session_id):
    if settings.GLOBAL_SETTINGS.get('default_image') in request.user.profile.image.path:
        return redirect('profile')
    else:
        candidate = Candidate.objects.get(pk=candidate_id)
        voting_session = VotingSession.objects.get(pk=voting_session_id)
        rows = VoteUser.objects.filter(voting_session=voting_session, user=request.user)

        if rows.count() == 0:
            user_vote = VoteUser(candidate=candidate, voting_session=voting_session, user=request.user)
            user_vote.save()
            messages.success(request, f'Your vote has been registered successfully!')
        else:
            messages.warning(request, f'Your already voted in this election!')

        return redirect(reverse('votedash', kwargs={'pk': voting_session_id}))


def generate_statistics_and_context(voting_session):
    labels, data = [], []
    votes = VoteUser.objects.all().filter(voting_session=voting_session)
    for candidate in voting_session.candidates.all():
        labels.append(candidate.name)
        data.append(len(list(filter(lambda c: c.candidate_id == candidate.pk, votes))))

    return labels, data
