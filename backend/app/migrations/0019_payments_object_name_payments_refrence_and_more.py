# Generated by Django 4.2 on 2024-11-01 16:37

import app.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_alter_authusermodel_first_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="object_name",
            field=models.CharField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="payments",
            name="refrence",
            field=models.CharField(default=""),
            preserve_default=False,
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