# Generated by Django 5.0.7 on 2024-10-25 11:27

import app.common.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_comment_alter_authusermodel_first_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reaction",
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
                ("object_id", models.UUIDField()),
                ("email", models.EmailField(max_length=254)),
                ("reaction", models.CharField(max_length=120)),
                ("object_name", models.CharField(max_length=220)),
            ],
            options={
                "abstract": False,
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