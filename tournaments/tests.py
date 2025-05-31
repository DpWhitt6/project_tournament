from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Tournament, Team, Registration

# Create your tests here.
class TournamentTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(username='admin', password='adminpass', is_staff=True)
        self.user = User.objects.create_user(username='player', password='playerpass')
        self.tournament = Tournament.objects.create(
            name="Test Tournament",
            description="A tournament for testing",
            start_date="2025-01-01",
            end_date="2025-01-05",
            tournament_type="individual",
            created_by=self.admin
        )

    def test_tournament_list_view(self):
        response = self.client.get(reverse('tournament_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Tournament")

    def test_tournament_detail_view(self):
        response = self.client.get(reverse('tournament_detail', args=[self.tournament.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tournament.description)

    def test_create_tournament_requires_admin(self):
        self.client.login(username='player', password='playerpass')
        response = self.client.get(reverse('create_tournament'))
        self.assertEqual(response.status_code, 403)

    def test_register_individual(self):
        self.client.login(username='player', password='playerpass')
        response = self.client.post(reverse('register_individual', args=[self.tournament.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertTrue(Registration.objects.filter(user=self.user, tournament=self.tournament).exists())