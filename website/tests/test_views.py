from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


from website.models import Testimonial, Course
from website.forms import TestimonialCreateForm


class PublicViewTest(TestCase):
    def test_login_required_to_create_testimonial(self):
        res = self.client.get(reverse("website:testimonial-create"))
        self.assertNotEquals(res.status_code, 200)

    def test_login_required_to_update_testimonial(self):
        res = self.client.get(reverse("website:testimonial-update", kwargs={"pk": 1}))
        self.assertNotEquals(res.status_code, 200)

    def test_login_required_to_delete_testimonial(self):
        res = self.client.get(reverse("website:testimonial-delete", kwargs={"pk": 1}))
        self.assertNotEquals(res.status_code, 200)

    def test_retrieve_testimonials(self):
        res = self.client.get(reverse("website:testimonial-list"))
        self.assertEqual(res.status_code, 200)
        testimonials = Testimonial.objects.all()
        self.assertEqual(list(res.context["testimonial_list"]), list(testimonials))
        self.assertTemplateUsed(res, "website/testimonial_list.html")

    def test_retrieve_list_of_courses(self):
        res = self.client.get(reverse("website:course-list"))
        self.assertEqual(res.status_code, 200)
        courses = Course.objects.all()
        self.assertEqual(list(res.context["course_list"]), list(courses))
        self.assertTemplateUsed(res, "website/course_list.html")

    def test_page_get_only_finance_courses(self):
        res = self.client.get(reverse("website:finance-list"))
        self.assertEqual(res.status_code, 200)
        fin_courses = Course.objects.filter(category__name__iexact="finance")
        self.assertEqual(list(res.context["course_list"]), list(fin_courses))
        self.assertTemplateUsed(res, "website/finance_list.html")


class PrivateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser', password='password123'
        )
        self.testimonial = Testimonial.objects.create(owner=self.user, comment="Test Comment")
        self.client.force_login(self.user)

    def test_delete_testimonial(self):
        res = self.client.post(reverse('website:testimonial-delete', kwargs={'pk': self.testimonial.pk}))
        self.assertEqual(res.status_code, 302)
        self.assertFalse(Testimonial.objects.filter(pk=self.testimonial.pk).exists())



