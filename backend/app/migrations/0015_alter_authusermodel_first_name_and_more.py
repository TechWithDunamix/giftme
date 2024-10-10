# Generated by Django 5.0.7 on 2024-10-09 19:14

import app.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0014_usermembership_full_price_and_more"),
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
        migrations.AlterModelTable(
            name="usermembership",
            table="User Membership !",
        ),
    ]