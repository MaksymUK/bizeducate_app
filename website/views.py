import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from datetime import timedelta


from .forms import (
    CourseSearchForm,
    AuthorCreateForm,
    TestimonialCreateForm,
    ContactForm,
)
from .models import Course, Trainer, Testimonial, Author


def get_one_week_from_now():
    return timezone.now().date() + timedelta(weeks=1)


def index(request: HttpRequest) -> HttpResponse:
    one_week_from_now = get_one_week_from_now()
    courses = Course.objects.filter(start_date__gt=one_week_from_now)[:3]
    testimonials = Testimonial.objects.all()
    context = {
        "courses": courses,
        "testimonials": testimonials,
    }
    return render(request, "website/index.html", context=context)


class ContactUsView(generic.FormView):
    form_class = ContactForm
    template_name = "website/contact_us.html"
    success_url = reverse_lazy('website:contact_us_success')

    def form_valid(self, form):
        send_mail(
            form.cleaned_data["company"],
            f"Message from {form.cleaned_data['name']} <{form.cleaned_data['email']}>\n\n"
            f"{form.cleaned_data['message']}",
            None,  # from email
            [os.getenv("RECIPIENT_EMAIL_ADDRESS")],
        )
        return super().form_valid(form)


def contact_us_success(request: HttpRequest) -> HttpResponse:
    return render(request, 'website/contact_us_success.html')


class CourseListView(generic.ListView):
    model = Course
    queryset = Course.objects.all()
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(CourseListView, self).get_context_data(**kwargs)
        categories = set(course.category for course in context["course_list"])
        title = self.request.GET.get("title", "")
        category = self.request.GET.get("category", "")
        city = self.request.GET.get("city", "")
        context.update(
            {
                "trainers": Trainer.objects.filter(category__in=categories),
                "search_form": CourseSearchForm(
                    initial={"title": title, "category": category, "city": city}
                ),
            }
        )
        return context

    def get_queryset(self):
        one_week_from_now = get_one_week_from_now()
        queryset = Course.objects.filter(start_date__gt=one_week_from_now)
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


class TestimonialListView(generic.ListView):
    model = Testimonial
    template_name = "website/testimonial_list.html"
    paginate_by = 5


class TestimonialCreateView(LoginRequiredMixin, generic.CreateView):
    model = Testimonial
    form_class = TestimonialCreateForm
    success_url = reverse_lazy("website:testimonial-list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TestimonialUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Testimonial
    fields = ["author_full_name", "author_company", "comment", "author_company_logo"]

    def get_success_url(self):
        return reverse_lazy(
            "website:author-detail", kwargs={"pk": self.object.owner.pk}
        )


class TestimonialDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Testimonial

    def get_success_url(self):
        return reverse_lazy(
            "website:author-detail", kwargs={"pk": self.object.owner.pk}
        )


class AuthorCreateView(generic.CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = "website/author_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.set_password(form.cleaned_data["password1"])
        self.object.save()
        return response

    def get_success_url(self):
        return reverse("website:author-detail", kwargs={"pk": self.object.pk})


class AuthorUpdateView(generic.UpdateView):
    model = Author
    fields = ["first_name", "last_name", "email"]

    def get_success_url(self):
        return self.object.get_absolute_url()


class AuthorDetailView(generic.DetailView):
    model = Author
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        testimonials = Testimonial.objects.filter(owner=self.object)
        paginator = Paginator(testimonials, self.paginate_by)
        page_number = self.request.GET.get("page")

        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context["testimonials"] = page_obj
        context["paginator"] = paginator
        context["page_obj"] = page_obj
        context["is_paginated"] = page_obj.has_other_pages()
        return context


class AuthorDeleteView(generic.DeleteView):
    model = Author
    template_name = "website/author_delete_confirmation.html"
    success_url = reverse_lazy("website:index")


class FinanceListView(CourseListView):
    template_name = "website/finance_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(category__name__iexact="finance")


class ProjectManagementListView(CourseListView):
    template_name = "website/project_management_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(category__name__iexact="project management")


class LawListView(CourseListView):
    template_name = "website/law_list.html"

    def get_queryset(self):
        return super().get_queryset().filter(category__name__iexact="corporate law")


class CgListView(CourseListView):
    template_name = "website/grc_list.html"

    def get_queryset(self):
        return (
            super().get_queryset().filter(category__name__iexact="grc")
        )


def about_us(request: HttpRequest) -> HttpResponse:
    testimonials = Testimonial.objects.all()
    context = {
        "testimonials": testimonials,
    }
    return render(request, "website/about_us.html", context=context)


def corporate(request: HttpRequest) -> HttpResponse:
    return render(request, "website/corporate_training.html")
