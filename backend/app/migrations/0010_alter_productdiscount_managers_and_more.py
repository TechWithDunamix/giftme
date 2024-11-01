# Generated by Django 4.2 on 2024-11-01 00:42

import app.common.validators
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_productdiscount_user_alter_authusermodel_first_name_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='productdiscount',
            managers=[
                ('query', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='authusermodel',
            name='first_name',
            field=models.CharField(max_length=125, validators=[app.common.validators.AuthValidators.validate_first_name]),
        ),
        migrations.AlterField(
            model_name='authusermodel',
            name='last_name',
            field=models.CharField(max_length=120, validators=[app.common.validators.AuthValidators.validate_last_name]),
        ),
    ]