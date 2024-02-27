from django.test import TestCase
from django.contrib.auth import get_user_model

from website.models import Venue, Category, Trainer, Course, Author, Testimonial


class ModelsTests(TestCase):

    def setUp(self):
        self.author = get_user_model().objects.create(
            username="test_john",
            password="test12345",
            first_name="John",
            last_name="Doe",
        )

    def test_venue_string_representation(self):
        venue = Venue(city="London", country="United Kingdom")
        self.assertEqual(str(venue), "London, United Kingdom")

    def test_category_string_representation(self):
        category = Category(name="Finance")
        self.assertEqual(str(category), "Finance")

    def test_trainer_string_representation(self):
        trainer = Trainer(
            first_name="Test_first",
            last_name="Test_last",
        )
        self.assertEqual(str(trainer), "Trainer: Test_first Test_last")

    def test_course_string_representation(self):
        course = Course(
            title="Test title",
        )
        self.assertEqual(str(course), "Test title")

    def test_author_string_representation(self):
        author = self.author
        self.assertEqual(
            str(author),
            f"{author.first_name} {author.last_name}",
        )

    def test_testimonial_string_representation(self):
        testimonial = Testimonial(
            author_full_name="Test Author",
            author_company="Test Company",
            comment="Test Comment",
        )
        self.assertEqual(str(testimonial), f"{testimonial.author_full_name}: {testimonial.comment}")
