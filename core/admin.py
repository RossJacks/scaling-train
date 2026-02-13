from django.contrib import admin

from .models import (
    Award,
    BusinessHour,
    LocationInfo,
    MenuCategory,
    MenuItem,
    Review,
    SpecialOffer,
    TeamMember,
    Testimonial,
)


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0


@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "display_style", "show_price", "ordering", "is_active")
    list_filter = ("display_style", "is_active")
    search_fields = ("name", "description")
    ordering = ("ordering", "name")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "ordering", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name", "description")
    ordering = ("category", "ordering", "name")


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ("title", "ordering", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "details")
    ordering = ("ordering", "title")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "ordering", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "quote")
    ordering = ("ordering", "name")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "ordering", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "role", "bio")
    ordering = ("ordering", "name")


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "organization", "ordering")
    list_filter = ("year",)
    search_fields = ("title", "organization")
    ordering = ("-year", "ordering", "title")


@admin.register(BusinessHour)
class BusinessHourAdmin(admin.ModelAdmin):
    list_display = ("day_label", "hours", "ordering", "is_active")
    list_filter = ("is_active",)
    search_fields = ("day_label", "hours")
    ordering = ("ordering", "day_label")


@admin.register(LocationInfo)
class LocationInfoAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "region", "phone", "email")
    search_fields = ("name", "city", "region", "phone", "email")


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "name", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("title", "name", "body")
    ordering = ("-created_at",)
