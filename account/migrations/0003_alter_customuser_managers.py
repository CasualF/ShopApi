# Generated by Django 4.2.3 on 2023-07-18 08:55

import account.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_alter_customuser_managers"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", account.models.UserManager()),
            ],
        ),
    ]