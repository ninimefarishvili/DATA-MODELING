# Generated by Django 5.1.2 on 2024-11-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("eventManager", "0004_alter_event_stadium"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]