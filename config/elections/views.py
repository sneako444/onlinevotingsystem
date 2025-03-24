from django.shortcuts import render, redirect
from .models import Election, Candidate, Vote
from django.contrib.auth.decorators import login_required

def list_elections(request):
    elections = Election.objects.all()
    return render(request, 'elections/list.html', {'elections': elections})

@login_required
def election_detail(request, election_id):
    election = Election.objects.get(id=election_id)
    candidates = Candidate.objects.filter(election=election)
    return render(request, 'elections/detail.html', {'election': election, 'candidates': candidates})

@login_required
def vote(request, candidate_id):
    candidate = Candidate.objects.get(id=candidate_id)
    vote, created = Vote.objects.get_or_create(user=request.user, candidate=candidate)
    candidate.votes += 1
    candidate.save()
    return redirect('election_detail', election_id=candidate.election.id)
