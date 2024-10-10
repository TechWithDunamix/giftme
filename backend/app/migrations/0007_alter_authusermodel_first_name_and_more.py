# Generated by Django 5.0.7 on 2024-10-06 21:09

import app.common.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_userpost_draft_userpost_exlusive_userpost_scheduled_and_more"),
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
            name="UserGalary",
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
                (
                    "images",
                    models.ManyToManyField(
                        related_name="user_galaries", to="app.images"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_galaries",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "User Galary",
            },
        ),
    ]