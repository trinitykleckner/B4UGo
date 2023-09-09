# Generated by Django 4.2.5 on 2023-09-09 17:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=255)),
                (
                    "attributes",
                    models.CharField(
                        choices=[("xxx", "xxx"), ("xxx", "xxx")], max_length=255
                    ),
                ),
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10),
                        ]
                    ),
                ),
                ("pos_text", models.CharField(max_length=500)),
                ("neg_text", models.CharField(max_length=500)),
                ("date", models.DateField(auto_now=True)),
            ],
        ),
    ]