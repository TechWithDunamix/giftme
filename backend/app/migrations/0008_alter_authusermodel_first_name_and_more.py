# Generated by Django 5.0.7 on 2024-10-28 15:28

import app.common.validators
import datetime
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_authusermodel_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authusermodel",
            name="first_name",
            field=models.CharField(
                max_length=125,
                validators=[app.common.validators.AuthValidators.validate_first_name],
            ),
        ),
        migrations.AlterField(
            model_name="authusermodel",
            name="last_name",
            field=models.CharField(
                max_length=120,
                validators=[app.common.validators.AuthValidators.validate_last_name],
            ),
        ),
        migrations.CreateModel(
            name="ProductDiscount",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now_add=True, null=True)),
                ("title", models.CharField(max_length=120)),
                ("percentage_or_price", models.FloatField()),
                (
                    "starting",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2024,
                            10,
                            28,
                            15,
                            28,
                            8,
                            363149,
                            tzinfo=datetime.timezone.utc,
                        )
                    ),
                ),
                ("ending", models.DateTimeField(null=True)),
                ("limit_quantity", models.BooleanField(default=False)),
                ("max_quantity", models.PositiveSmallIntegerField(null=True)),
                (
                    "discount_type",
                    models.CharField(default="percentage", max_length=250),
                ),
                (
                    "products",
                    models.ManyToManyField(
                        related_name="discounts", to="app.productlist"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]