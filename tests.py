from django.test import TestCase
from django.urls import reverse
from .models import Yangilik
# Create your tests here.
class YangilikModelTest(TestCase):
    def setUp(self):
        Yangilik.objects.create(title="Mavzu", text="Mavzu matni")

    def test_text_content(self):
        post = Yangilik.objects.get(id=1)
        expected_object_title = f'{post.title}'
        expected_object_text = f'{post.text}'
        self.assertEqual(expected_object_title, "Mavzu")
        self.assertEqual(expected_object_text, "Mavzu matni")

class HomePageViewTest(TestCase):
    def setUp(self):
        Yangilik.objects.create(title="Mavzu-2", text="Mavzu-2 matni")

    def test_views_urls_exits_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')