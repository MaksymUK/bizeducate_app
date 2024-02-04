from django.urls import path
from .views import index, contact_us, CourseListView, CourseDetailView, FinanceListView

urlpatterns = [
    path("", index, name="index"),
    path("contact_us/", contact_us, name="contact-us"),
    path("courses/", CourseListView.as_view(), name="course-list"),
    path("courses/<int:pk>/", CourseDetailView.as_view(), name="course-detail"),
    path("finance/", FinanceListView.as_view(), name="finance-list"),
]

app_name = "website"
