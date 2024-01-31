from django.urls import path
from .views import index, contact_us

urlpatterns = [
    path("", index, name="index"),
    path("contact_us/", contact_us, name="contact-us")
]

app_name = "website"
