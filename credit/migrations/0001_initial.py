# Generated by Django 4.0.5 on 2023-03-31 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LoanRequest",
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
                ("personal_id", models.CharField(max_length=20)),
                ("dni", models.CharField(max_length=20)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("gender", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                (
                    "requested_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("approved", models.BooleanField(default=False)),
            ],
        ),
    ]
