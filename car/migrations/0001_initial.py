# Generated by Django 4.1 on 2024-12-02 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("manufacturer", models.CharField(max_length=64)),
                ("model", models.CharField(max_length=64)),
                (
                    "horse_powers",
                    models.PositiveSmallIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(1914),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("is_broken", models.BooleanField()),
                ("problem_description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
