from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=80)
    title = models.CharField(max_length=120)
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} - {self.name}"


class MenuCategory(models.Model):
    DISPLAY_TABLE = "table"
    DISPLAY_DEFINITION = "definition"
    DISPLAY_LIST = "list"
    DISPLAY_CHOICES = [
        (DISPLAY_TABLE, "Table"),
        (DISPLAY_DEFINITION, "Definition list"),
        (DISPLAY_LIST, "List"),
    ]

    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    display_style = models.CharField(
        max_length=20, choices=DISPLAY_CHOICES, default=DISPLAY_LIST
    )
    ordered_list = models.BooleanField(default=False)
    show_price = models.BooleanField(default=False)
    ordering = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordering", "name"]

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(
        MenuCategory, related_name="items", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    ordering = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordering", "name"]

    def __str__(self) -> str:
        return self.name


class SpecialOffer(models.Model):
    title = models.CharField(max_length=120)
    details = models.TextField()
    ordering = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordering", "title"]

    def __str__(self) -> str:
        return self.title


class Testimonial(models.Model):
    quote = models.TextField()
    name = models.CharField(max_length=80)
    ordering = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordering", "name"]

    def __str__(self) -> str:
        return f"{self.name} testimonial"


class TeamMember(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    bio = models.TextField()
    image_url = models.URLField(blank=True)
    ordering = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordering", "name"]

    def __str__(self) -> str:
        return self.name


class Award(models.Model):
    year = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=160)
    organization = models.CharField(max_length=160)
    ordering = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["-year", "ordering", "title"]

    def __str__(self) -> str:
        return f"{self.year} {self.title}"


class BusinessHour(models.Model):
    day_label = models.CharField(max_length=80)
    hours = models.CharField(max_length=120)
    ordering = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordering", "day_label"]

    def __str__(self) -> str:
        return f"{self.day_label}: {self.hours}"


class LocationInfo(models.Model):
    name = models.CharField(max_length=120)
    address_line1 = models.CharField(max_length=160)
    address_line2 = models.CharField(max_length=160, blank=True)
    city = models.CharField(max_length=80)
    region = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=40)
    email = models.EmailField()

    class Meta:
        verbose_name = "location info"
        verbose_name_plural = "location info"

    def __str__(self) -> str:
        return self.name
