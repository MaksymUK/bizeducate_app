from django.db import models


class Venue(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")

    class Meta:
        ordering = ["country"]

    def __str__(self):
        return f"{self.city}, {self.country}"


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Trainer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    qualification = models.CharField(max_length=500, blank=True)
    profile = models.TextField(max_length=1000, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, related_name="trainers")
    trainer_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"Trainer: {self.first_name} {self.last_name}"


class Course(models.Model):
    title = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, related_name="courses")
    venue = models.ForeignKey(Venue, on_delete=models.DO_NOTHING, blank=True, related_name="courses")
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    overview = models.TextField(max_length=500, blank=True)
    trainers = models.ManyToManyField(Trainer, related_name="courses")

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return self.title
