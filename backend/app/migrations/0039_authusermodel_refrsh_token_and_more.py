# Generated by Django 4.2 on 2024-11-12 17:58

import app.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0038_alter_authusermodel_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="authusermodel",
            name="refrsh_token",
            field=models.CharField(max_length=160, null=True),
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