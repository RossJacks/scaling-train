from django.db.models import Prefetch
from django.shortcuts import redirect, render

from .forms import ReviewForm
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


def home(request):
    return render(
        request,
        "home.html",
        {
            "testimonials": Testimonial.objects.filter(is_active=True),
            "location": LocationInfo.objects.first(),
            "hours": BusinessHour.objects.filter(is_active=True),
        },
    )


def menu(request):
    items_qs = MenuItem.objects.filter(is_active=True)
    categories = MenuCategory.objects.filter(is_active=True).prefetch_related(
        Prefetch("items", queryset=items_qs)
    )
    category_map = {category.slug: category for category in categories}
    return render(
        request,
        "menu.html",
        {
            "rotisserie_category": category_map.get("rotisserie"),
            "sides_category": category_map.get("sides"),
            "beverages_category": category_map.get("beverages"),
            "desserts_category": category_map.get("desserts"),
            "special_offers": SpecialOffer.objects.filter(is_active=True),
        },
    )


def about(request):
    return render(
        request,
        "about.html",
        {
            "team": TeamMember.objects.filter(is_active=True),
            "awards": Award.objects.all(),
            "location": LocationInfo.objects.first(),
            "hours": BusinessHour.objects.filter(is_active=True),
        },
    )


def reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reviews")
    else:
        form = ReviewForm()
    return render(
        request,
        "reviews.html",
        {"reviews": Review.objects.all(), "form": form},
    )
