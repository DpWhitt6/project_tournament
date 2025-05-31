from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Profile

# Create your tests here.
class AccountTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_profile_created(self):
        profile = Profile.objects.create(user=self.user, bio="Test Bio")
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.bio, 'Test Bio')

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_profile_view_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertRedirects(response, '/accounts/login/?next=/accounts/profile/')

    def test_profile_view_logged_in(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')