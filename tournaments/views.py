from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Tournament, Registration
from .forms import TournamentForm, TeamRegistrationForm, IndividualRegistrationForm

# Create your views here.
def is_admin(user):
    return user.is_staff

def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'tournaments/tournament_list.html', {'tournaments': tournaments})

def tournament_detail(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    return render(request, 'tournaments/tournament_detail.html', {'tournament': tournament})

@user_passes_test(is_admin)
@login_required
def create_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.created_by = request.user
            tournament.save()
            messages.success(request, 'Tournament created successfully.')
            return redirect('tournament_list')
    else:
        form = TournamentForm()
    return render(request, 'tournaments/tournament_form.html', {'form': form})

@login_required
def register_team(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            team = form.save()
            Registration.objects.create(user=request.user, tournament=tournament, team=team)
            messages.success(request, 'Team registered successfully.')
            return redirect('tournament_detail', pk=pk)
    else:
        form = TeamRegistrationForm()
    return render(request, 'tournaments/register_team.html', {'form': form, 'tournament': tournament})

@login_required
def register_individual(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == 'POST':
        form = IndividualRegistrationForm(request.POST)
        if form.is_valid():
            Registration.objects.create(user=request.user, tournament=tournament)
            messages.success(request, 'Registered successfully.')
            return redirect('tournament_detail', pk=pk)
    else:
        form = IndividualRegistrationForm()
    return render(request, 'tournaments/register_individual.html', {'form': form, 'tournament': tournament})