from django.test import TestCase
from website.models import Category

from website.forms import CourseSearchForm, AuthorCreateForm, TestimonialCreateForm, ContactForm


# class FormsTest(TestCase):
#     def test_testimonial_create_form(self):
#         form_data = {
#             "author_full_name": "Test Author",
#             "author_company": "Test Company",
#             "comment": "Test Comment",
#             "author_company_logo": "Test Logo",
#         }
#         form = TestimonialCreateForm(data=form_data)
#         self.assertTrue(form.is_valid())
#         self.assertEqual(form.cleaned_data, form_data)
