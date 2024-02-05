from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from .forms import CourseSearchForm
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
        context = super(CourseListView, self).get_context_data(**kwargs)
        categories = set(course.category for course in context['course_list'])
        title = self.request.GET.get("title", "")
        category = self.request.GET.get("category", "")
        city = self.request.GET.get("city", "")
        context.update({
            "trainers": Trainer.objects.filter(category__in=categories),
            "search_form": CourseSearchForm(initial={"title": title, "category": category, "city": city})
        })
        return context

    def get_queryset(self):
        queryset = Course.objects.all()
        form = CourseSearchForm(self.request.GET)
        if form.is_valid():
            title_query = form.cleaned_data.get("title", "")
            category_query = form.cleaned_data.get("category")
            city_query = form.cleaned_data.get("city", "")

            if title_query:
                queryset = queryset.filter(title__icontains=title_query)
            if category_query:
                queryset = queryset.filter(category=category_query)
            if city_query:
                queryset = queryset.filter(venue__city__icontains=city_query)

        return queryset


class CourseDetailView(generic.DetailView):
    model = Course


class FinanceListView(CourseListView):
    template_name = "website/finance_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(category__name__iexact="finance")

