from django import forms
from .models import Tournament, Team, Registration

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'description', 'start_date', 'end_date', 'tournament_type']

class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members']
        widgets = {
            'members': forms.CheckboxSelectMultiple
        }

class IndividualRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = []