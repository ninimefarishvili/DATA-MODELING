# Generated by Django 5.1.2 on 2024-10-31 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                (
                    "username",
                    models.CharField(max_length=100, verbose_name="iuzerneimi"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="ელ.ფოსტის მისამართი"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="აქტიურია"),
                ),
            ],
            options={
                "verbose_name": "მომხმარებელი",
                "verbose_name_plural": "მომხმარებლები",
                "ordering": ("-id",),
            },
        ),
        migrations.CreateModel(
            name="Stadium",
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
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("capacity", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Event",
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
                ("name", models.CharField(max_length=100)),
                ("date", models.DateTimeField()),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="აქტიურია"),
                ),
                (
                    "stadium",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="eventManager.stadium",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
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
                ("bought_at", models.DateTimeField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="eventManager.customer",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="eventManager.event",
                    ),
                ),
            ],
        ),
    ]
