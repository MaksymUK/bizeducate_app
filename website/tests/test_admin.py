from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin_user", password="testadmin123"
        )
        self.client.force_login(self.admin_user)
        self.author = get_user_model().objects.create_user(
            username="author",
            password="testauthor123",
        )

    def test_author_listed(self):
        url = reverse("admin:website_author_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.author.username)

    def test_author_change_page(self):
        url = reverse("admin:website_author_change", args=[self.author.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_create_author_page(self):
        url = reverse("admin:website_author_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_testimonial_has_author_foreign_key(self):
        url = reverse("admin:website_testimonial_add")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "owner")
