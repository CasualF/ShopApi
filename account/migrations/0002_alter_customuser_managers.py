# Generated by Django 4.2.3 on 2023-07-18 08:50

import account.models
import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("a", account.models.UserManager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]