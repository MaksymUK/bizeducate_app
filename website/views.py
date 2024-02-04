from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .models import Course, Trainer


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = set(course.category for course in context['course_list'])
        context['trainers'] = Trainer.objects.filter(category__in=categories)
        return context


class CourseDetailView(generic.DetailView):
    model = Course


class FinanceListView(CourseListView):
    template_name = "website/finance_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(category__name__iexact="finance")

