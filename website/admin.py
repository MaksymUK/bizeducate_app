from django.contrib import admin

from website.models import Venue, Category, Trainer, Course


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ["city", "country"]
    list_filter = ["country"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "category",]
    list_filter = ["category"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "venue", "start_date", "category",]
    list_filter = ["category", "venue"]
