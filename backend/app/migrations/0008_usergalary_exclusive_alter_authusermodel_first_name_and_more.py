# Generated by Django 5.0.7 on 2024-10-07 10:02

import app.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_authusermodel_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="usergalary",
            name="exclusive",
            field=models.BooleanField(default=False),
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
