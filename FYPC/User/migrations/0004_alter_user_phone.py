# Generated by Django 4.1.5 on 2023-01-12 01:41

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ("User", "0003_user_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None
            ),
        ),
    ]
