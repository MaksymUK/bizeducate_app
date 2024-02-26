from website.models import Author, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from PIL import Image
import io

from website.forms import CourseSearchForm, AuthorCreateForm, TestimonialCreateForm, ContactForm


class FormsTest(TestCase):
    def setUp(self):
        self.user = Author.objects.create(username='test_user')
        self.category = Category.objects.create(id=1, name="Finance")

    def test_testimonial_create_form_with_valid_form(self):

        form_data = {
            "owner": self.user.id,
            "author_full_name": "John Doe",
            "author_company": "Acme Inc",
            "author_position": "CEO",
            "comment": "This is a test comment."
        }

        image_data = io.BytesIO()
        Image.new('RGB', (100, 100)).save(image_data, format='JPEG')
        image_data.seek(0)

        uploaded_file = SimpleUploadedFile("test_image.jpg", image_data.read(), content_type='image/jpeg')
        form = TestimonialCreateForm(data=form_data, files={"author_company_logo": uploaded_file})

        self.assertTrue(form.is_valid())

    def test_testimonial_create_form_with_invalid_form(self):
        form_data = {}
        form = TestimonialCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("author_full_name", form.errors)
        self.assertIn("author_company", form.errors)
        self.assertIn("comment", form.errors)

    def test_testimonial_create_form_with_invalid_file_type(self):
        form_data = {
            "owner": self.user.id,
            "author_full_name": "John Doe",
            "author_company": "Acme Inc",
            "author_position": "CEO",
            "comment": "This is a test comment."
        }

        file_content = b"This is a text file."
        uploaded_file = SimpleUploadedFile("test_file.txt", file_content, content_type='text/plain')

        form = TestimonialCreateForm(data=form_data, files={"author_company_logo": uploaded_file})

        self.assertFalse(form.is_valid())
        # Assert that the correct error message is raised for the invalid file type
        self.assertIn("author_company_logo", form.errors)
        self.assertEqual(form.errors["author_company_logo"],
                         ["Upload a valid image. The file you uploaded was either not an image or a corrupted image."])

    def test_contact_form(self):
        form_data = {
            "name": "Test Name",
            "email": "test_name@yahoo.com",
            "company": "Test Company",
            "message": "Test Message",
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_contact_form_without_completed_fields(self):
        form_data = {}
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)
        self.assertIn("email", form.errors)
        self.assertIn("company", form.errors)
        self.assertIn("message", form.errors)

    def test_author_create_form(self):
        form_data = {
            "username": "test_3",
            "first_name": "Test Name",
            "last_name": "Test Surname",
            "email": "test_name@yahoo.com",
            "password1": "User123!_k",
            "password2": "User123!_k",
        }
        form = AuthorCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_course_search_form_by_title(self):
        form_data = {
            "title": "Test Title",
            "category": None,
            "city": "",
        }
        form = CourseSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_course_search_form_by_category(self):
        form_data = {
            "title": "",
            "category": self.category,
            "city": "",
        }
        form = CourseSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_course_search_form_by_city(self):
        form_data = {
            "title": "",
            "category": None,
            "city": "London"
        }
        form = CourseSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
