from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class ViewsTestCase(TestCase):
    """とりあえずすべてのdd_appページがステータスコードで200で帰ってくるか否かをテストする。"""

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_post_movie_view(self):
        response = self.client.get(reverse("post_movie"))
        self.assertEqual(response.status_code, 200)

    def test_setup_tag_view(self):
        response = self.client.get(reverse("setup_tag"))
        self.assertEqual(response.status_code, 200)

    def test_show_video_detail_view(self):
        response = self.client.get(reverse("show_video_detail"))
        self.assertEqual(response.status_code, 200)
