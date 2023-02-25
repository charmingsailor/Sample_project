from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from django.test import SimpleTestCase


class HomepageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')

    def test_for_title(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, '<h1>Programming Languages</h1>')
    def test_for_cards(self):
        responss = self.client.get(reverse('home'))
        self.assertContains(responss, '<div class="card">',count=3)


class AboutpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")


class PythonpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/python/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("python"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("python"))
        self.assertTemplateUsed(response, "python.html")


class FsharppageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/fsharp/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("fsharp"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("fsharp"))
        self.assertTemplateUsed(response, "fsharp.html")


class RacketpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/racket/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("racket"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("racket"))
        self.assertTemplateUsed(response, "racket.html")
