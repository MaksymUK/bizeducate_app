from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .models import Course


def index(request: HttpRequest) -> HttpResponse:
    courses = Course.objects.all()[0:3]
    context = {
        "courses": courses
    }
    return render(request, "website/index.html", context=context)
