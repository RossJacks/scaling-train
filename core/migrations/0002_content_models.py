from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Award",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("year", models.PositiveSmallIntegerField()),
                ("title", models.CharField(max_length=160)),
                ("organization", models.CharField(max_length=160)),
                ("ordering", models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                "ordering": ["-year", "ordering", "title"],
            },
        ),
        migrations.CreateModel(
            name="BusinessHour",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("day_label", models.CharField(max_length=80)),
                ("hours", models.CharField(max_length=120)),
                ("ordering", models.PositiveSmallIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["ordering", "day_label"],
            },
        ),
        migrations.CreateModel(
            name="LocationInfo",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("address_line1", models.CharField(max_length=160)),
                ("address_line2", models.CharField(blank=True, max_length=160)),
                ("city", models.CharField(max_length=80)),
                ("region", models.CharField(max_length=80)),
                ("postal_code", models.CharField(max_length=20)),
                ("phone", models.CharField(max_length=40)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "verbose_name": "location info",
                "verbose_name_plural": "location info",
            },
        ),
        migrations.CreateModel(
            name="MenuCategory",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("slug", models.SlugField(unique=True)),
                ("description", models.TextField(blank=True)),
                ("image_url", models.URLField(blank=True)),
                (
                    "display_style",
                    models.CharField(
                        choices=[("table", "Table"), ("definition", "Definition list"), ("list", "List")],
                        default="list",
                        max_length=20,
                    ),
                ),
                ("ordered_list", models.BooleanField(default=False)),
                ("show_price", models.BooleanField(default=False)),
                ("ordering", models.PositiveSmallIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["ordering", "name"],
            },
        ),
        migrations.CreateModel(
            name="SpecialOffer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=120)),
                ("details", models.TextField()),
                ("ordering", models.PositiveSmallIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["ordering", "title"],
            },
        ),
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("role", models.CharField(max_length=120)),
                ("bio", models.TextField()),
                ("image_url", models.URLField(blank=True)),
                ("ordering", models.PositiveSmallIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["ordering", "name"],
            },
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quote", models.TextField()),
                ("name", models.CharField(max_length=80)),
                ("ordering", models.PositiveSmallIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "ordering": ["ordering", "name"],
            },
        ),
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ("ordering", models.PositiveSmallIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(on_delete=models.deletion.CASCADE, related_name="items", to="core.menucategory"),
                ),
            ],
            options={
                "ordering": ["ordering", "name"],
            },
        ),
    ]
