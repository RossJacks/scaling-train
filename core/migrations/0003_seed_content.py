from django.db import migrations


def seed_content(apps, schema_editor):
    Award = apps.get_model("core", "Award")
    BusinessHour = apps.get_model("core", "BusinessHour")
    LocationInfo = apps.get_model("core", "LocationInfo")
    MenuCategory = apps.get_model("core", "MenuCategory")
    MenuItem = apps.get_model("core", "MenuItem")
    SpecialOffer = apps.get_model("core", "SpecialOffer")
    TeamMember = apps.get_model("core", "TeamMember")
    Testimonial = apps.get_model("core", "Testimonial")

    if not LocationInfo.objects.exists():
        LocationInfo.objects.create(
            name="Ross' Rotisserie",
            address_line1="123 Chicken Lane",
            city="Foodville",
            region="FV",
            postal_code="12345",
            phone="(555) 123-4567",
            email="info@rossrotisserie.com",
        )

    if not BusinessHour.objects.exists():
        BusinessHour.objects.bulk_create(
            [
                BusinessHour(day_label="Monday - Friday", hours="11:00 AM - 9:00 PM", ordering=1),
                BusinessHour(day_label="Saturday - Sunday", hours="10:00 AM - 10:00 PM", ordering=2),
            ]
        )

    if not Award.objects.exists():
        Award.objects.bulk_create(
            [
                Award(year=2026, title="Best Rotisserie Chicken", organization="Foodville Restaurant Association", ordering=1),
                Award(year=2025, title="People's Choice Award", organization="Local Food Festival", ordering=2),
                Award(year=2024, title="Best New Restaurant", organization="City Magazine", ordering=3),
                Award(year=2023, title="Excellence in Service", organization="Chamber of Commerce", ordering=4),
            ]
        )

    if not TeamMember.objects.exists():
        TeamMember.objects.bulk_create(
            [
                TeamMember(
                    name="Ross Jackson",
                    role="Owner & Head Chef",
                    bio="With over 20 years of culinary experience, Ross brings his expertise and passion to every dish. His secret spice blend is what makes our rotisserie chicken truly special.",
                    image_url="https://picsum.photos/300/300?random=5",
                    ordering=1,
                ),
                TeamMember(
                    name="Maria Rodriguez",
                    role="Kitchen Manager",
                    bio="Maria ensures that every chicken is cooked to perfection. Her attention to detail and dedication to quality control makes her an invaluable member of our team.",
                    image_url="https://picsum.photos/300/300?random=6",
                    ordering=2,
                ),
                TeamMember(
                    name="Tom Chen",
                    role="Customer Service Lead",
                    bio="Tom's friendly smile and exceptional customer service keep our guests coming back. He's always ready to help you find the perfect meal.",
                    image_url="https://picsum.photos/300/300?random=7",
                    ordering=3,
                ),
            ]
        )

    if not Testimonial.objects.exists():
        Testimonial.objects.bulk_create(
            [
                Testimonial(
                    quote="The best chicken I've ever had! The skin is so crispy and the meat is so tender.",
                    name="Sarah M.",
                    ordering=1,
                ),
                Testimonial(
                    quote="Ross' Rotisserie has become our family's go-to spot for dinner. We love everything on the menu!",
                    name="John D.",
                    ordering=2,
                ),
            ]
        )

    if not MenuCategory.objects.exists():
        rotisserie = MenuCategory.objects.create(
            name="Rotisserie Chicken",
            slug="rotisserie",
            description="Chicken Options",
            display_style="table",
            show_price=True,
            ordering=1,
        )
        sides = MenuCategory.objects.create(
            name="Side Dishes",
            slug="sides",
            image_url="https://picsum.photos/600/300?random=3",
            display_style="definition",
            ordering=2,
        )
        beverages = MenuCategory.objects.create(
            name="Beverages",
            slug="beverages",
            display_style="list",
            ordering=3,
        )
        desserts = MenuCategory.objects.create(
            name="Desserts",
            slug="desserts",
            display_style="list",
            ordered_list=True,
            ordering=4,
        )

        MenuItem.objects.bulk_create(
            [
                MenuItem(category=rotisserie, name="Whole Chicken", description="Perfectly seasoned whole chicken", price=12.99, ordering=1),
                MenuItem(category=rotisserie, name="Half Chicken", description="Half a rotisserie chicken", price=7.99, ordering=2),
                MenuItem(category=rotisserie, name="Quarter Chicken", description="White or dark meat quarter", price=4.99, ordering=3),
                MenuItem(category=rotisserie, name="Family Pack", description="2 whole chickens + 4 sides", price=29.99, ordering=4),
                MenuItem(category=sides, name="Mashed Potatoes", description="Creamy, buttery mashed potatoes with gravy", ordering=1),
                MenuItem(category=sides, name="Coleslaw", description="Fresh cabbage slaw with our special dressing", ordering=2),
                MenuItem(category=sides, name="Corn on the Cob", description="Grilled corn with butter and herbs", ordering=3),
                MenuItem(category=sides, name="Green Beans", description="Seasoned green beans with almonds", ordering=4),
                MenuItem(category=sides, name="Mac and Cheese", description="Classic creamy macaroni and cheese", ordering=5),
                MenuItem(category=sides, name="Caesar Salad", description="Fresh romaine lettuce with Caesar dressing and croutons", ordering=6),
                MenuItem(category=beverages, name="Soft Drinks (Coke, Pepsi, Sprite, etc.)", ordering=1),
                MenuItem(category=beverages, name="Iced Tea (Sweet or Unsweet)", ordering=2),
                MenuItem(category=beverages, name="Lemonade", ordering=3),
                MenuItem(category=beverages, name="Bottled Water", ordering=4),
                MenuItem(category=beverages, name="Coffee", ordering=5),
                MenuItem(category=desserts, name="Apple Pie", ordering=1),
                MenuItem(category=desserts, name="Chocolate Cake", ordering=2),
                MenuItem(category=desserts, name="Cookies (Chocolate Chip, Oatmeal Raisin)", ordering=3),
                MenuItem(category=desserts, name="Ice Cream (Vanilla, Chocolate, Strawberry)", ordering=4),
            ]
        )

    if not SpecialOffer.objects.exists():
        SpecialOffer.objects.bulk_create(
            [
                SpecialOffer(title="Tuesday Special", details="Buy one whole chicken, get a free side dish!", ordering=1),
                SpecialOffer(title="Weekend Deal", details="Family pack only $24.99 (save $5!)", ordering=2),
            ]
        )


def unseed_content(apps, schema_editor):
    Award = apps.get_model("core", "Award")
    BusinessHour = apps.get_model("core", "BusinessHour")
    LocationInfo = apps.get_model("core", "LocationInfo")
    MenuCategory = apps.get_model("core", "MenuCategory")
    MenuItem = apps.get_model("core", "MenuItem")
    SpecialOffer = apps.get_model("core", "SpecialOffer")
    TeamMember = apps.get_model("core", "TeamMember")
    Testimonial = apps.get_model("core", "Testimonial")

    Award.objects.all().delete()
    BusinessHour.objects.all().delete()
    LocationInfo.objects.all().delete()
    MenuItem.objects.all().delete()
    MenuCategory.objects.all().delete()
    SpecialOffer.objects.all().delete()
    TeamMember.objects.all().delete()
    Testimonial.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_content_models"),
    ]

    operations = [
        migrations.RunPython(seed_content, unseed_content),
    ]
