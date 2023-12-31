# Generated by Django 4.2.4 on 2023-08-20 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("donations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donation",
            name="frequency",
            field=models.CharField(
                choices=[
                    ("One-time", "One-time"),
                    ("Monthly", "Monthly"),
                    ("Annually", "Annually"),
                ],
                default="One-time",
                max_length=20,
            ),
        ),
    ]
