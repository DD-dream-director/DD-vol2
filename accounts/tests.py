from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your tests here.


class SignUpViewTests(TestCase):
    """アカウント登録バックエンドのテストコード"""

    def test_signup_page_status_code(self):
        """ページが存在するか否か"""
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_template(self):
        """指定されたテンプレートが指定されているか"""
        response = self.client.get(reverse("signup"))
        self.assertTemplateUsed(response, "register_user.html")

    def test_signup_form(self):
        """フォームを使用したサインアップの動作が可能か -> DBに登録できてるか否か"""
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

    def test_signup_redirect(self):
        """サインアップ後にタグのセッティングページにリダイレクトできているかを確認する。"""
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
        self.assertRedirects(response, reverse("login"))


class LoginViewTests(TestCase):
    """ログインバックエンドのテストコード"""

    def setUp(self):
        self.username = "testuser"
        self.password = "Testpass123"
        self.user = get_user_model().objects.create_user(
            username=self.username, password=self.password
        )

    def test_login_page_status_code(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)

    def test_login_page_template(self):
        response = self.client.get(reverse("login"))
        self.assertTemplateUsed(response, "login.html")

    def test_login_form_valid(self):
        response = self.client.post(
            reverse("login"), {"username": self.username,
                               "password": self.password}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))

    def test_login_form_invalid(self):
        response = self.client.post(
            reverse("login"), {"username": self.username,
                               "password": "wrongpassword"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["user"].is_authenticated)

    # ページ遷移のテスト
    def test_login_redirect(self):
        response = self.client.post(
            reverse("login"), {"username": self.username,
                               "password": self.password}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("home"))
