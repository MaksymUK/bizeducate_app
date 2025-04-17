from django.urls import path
from .views import (
    index,
    ContactUsView,
    contact_us_success,
    CourseListView,
    CourseDetailView,
    FinanceListView,
    TestimonialListView,
    AuthorCreateView,
    AuthorDetailView,
    AuthorUpdateView,
    AuthorDeleteView,
    TestimonialCreateView,
    TestimonialDeleteView,
    TestimonialUpdateView,
    LawListView,
    CgListView,
    ProcurementListView,
    about_us,
    corporate,
)

urlpatterns = [
    path("", index, name="index"),
    path("contact_us/", ContactUsView.as_view(), name="contact-us"),
    path("contact_us_success/", contact_us_success, name='contact_us_success'),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("testimonials/", TestimonialListView.as_view(), name="testimonial-list"),
    path(
        "testimonials/create/",
        TestimonialCreateView.as_view(),
        name="testimonial-create",
    ),
    path(
        "testimonials/<int:pk>/update/",
        TestimonialUpdateView.as_view(),
        name="testimonial-update",
    ),
    path(
        "testimonials/<int:pk>/delete/",
        TestimonialDeleteView.as_view(),
        name="testimonial-delete",
    ),
    path("authors/create/", AuthorCreateView.as_view(), name="author-create"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("authors/<int:pk>/update/", AuthorUpdateView.as_view(), name="author-update"),
    path("authors/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),
    path("finance/", FinanceListView.as_view(), name="finance-list"),
    path("procurement/", ProcurementListView.as_view(), name="procurement-list"),
    path("law/", LawListView.as_view(), name="law-list"),
    path("grc/", CgListView.as_view(), name="grc-list"),
    path("about/", about_us, name="about"),
    path("corporate/", corporate, name="corporate"),
]

app_name = "website"
