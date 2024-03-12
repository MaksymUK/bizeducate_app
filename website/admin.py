from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from website.models import Venue, Category, Trainer, Course, Author, Testimonial


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ["city", "country", "venue_image"]
    list_filter = ["country"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "category",
    ]
    list_filter = ["category"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "venue",
        "start_date",
        "category",
    ]
    list_filter = ["category", "venue"]


@admin.register(Author)
class AuthorAdmin(UserAdmin):
    list_display = ["first_name", "last_name", "username"]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["comment", "date", "owner", "author_full_name"]


admin.site.unregister(Group)
