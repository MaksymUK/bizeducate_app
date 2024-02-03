from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .models import Course


def index(request: HttpRequest) -> HttpResponse:
    courses = Course.objects.all()[0:3]
    context = {
        "courses": courses,
        'transparent_header': True,
    }
    return render(request, "website/index.html", context=context)


def contact_us(request: HttpRequest) -> HttpResponse:
    return render(request, "website/contact_us.html")


class CourseListView(generic.ListView):
    model = Course
    queryset = Course.objects.all()
    paginate_by = 5


class CourseDetailView(generic.DetailView):
    model = Course
