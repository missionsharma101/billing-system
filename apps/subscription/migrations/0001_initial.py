# Generated by Django 4.1.4 on 2022-12-23 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("billmanagement", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Subscription",
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
                    "status",
                    models.CharField(
                        choices=[("paid", "paid"), ("unpaid", "unpaid")], max_length=15
                    ),
                ),
                ("amount", models.FloatField(null=True)),
                ("from_date", models.DateField(auto_now_add=True)),
                ("to_date", models.DateField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="billmanagement.customer",
                    ),
                ),
            ],
        ),
    ]
