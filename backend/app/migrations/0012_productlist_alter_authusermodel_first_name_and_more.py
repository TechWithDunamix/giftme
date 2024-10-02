# Generated by Django 5.0.7 on 2024-10-02 22:52

import app.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0011_alter_authusermodel_first_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductList",
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
                ("name", models.CharField(max_length=150)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=9)),
                ("categories", models.JSONField(default=list)),
                ("image", models.ImageField(upload_to="product_images")),
                (
                    "confirmation_massage",
                    models.TextField(default="Product ordered !!!"),
                ),
                ("setting", models.JSONField(default=dict)),
                ("draft", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "Products",
            },
        ),
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
    ]
