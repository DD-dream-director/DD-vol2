from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.


class SignUpViewTests(TestCase):

    def test_signup_page_status_code(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_template(self):
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "register_user.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "test@example.com",
                "password1": "Testpass123",
                "password2": "Testpass123",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="testuser").exists())
