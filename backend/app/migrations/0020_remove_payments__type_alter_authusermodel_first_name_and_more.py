# Generated by Django 4.2 on 2024-11-01 17:37

import app.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0019_payments_object_name_payments_refrence_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payments",
            name="_type",
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