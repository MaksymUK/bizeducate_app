from django.urls import path
from .views import (index, contact_us, CourseListView, CourseDetailView, FinanceListView, TestimonialListView,
                    AuthorCreateView, AuthorDetailView, AuthorUpdateView, AuthorDeleteView, TestimonialCreateView,
                    TestimonialDeleteView, TestimonialUpdateView)

urlpatterns = [
    path("", index, name="index"),
    path("contact_us/", contact_us, name="contact-us"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("testimonials/", TestimonialListView.as_view(), name="testimonial-list"),
    path("testimonials/create/", TestimonialCreateView.as_view(), name="testimonial-create"),
    path("testimonials/<int:pk>/update/", TestimonialUpdateView.as_view(), name="testimonial-update"),
    path("testimonials/<int:pk>/delete/", TestimonialDeleteView.as_view(), name="testimonial-delete"),
    path("authors/create/", AuthorCreateView.as_view(), name="author-create"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/<int:pk>/update/", AuthorUpdateView.as_view(), name="author-update"),
    path("authors/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),
    path("finance/", FinanceListView.as_view(), name="finance-list"),
]

app_name = "website"
