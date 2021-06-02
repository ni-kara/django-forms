from django.test import SimpleTestCase
from django.urls import reverse, resolve
from forms.views import login, registration, dashboard

class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)

    def test_registration_url(self):
        url = reverse('registration')
        self.assertEqual(resolve(url).func, registration)

    def test_dashboard_url(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func, dashboard)



