# Generated by Django 4.1.5 on 2023-01-12 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Image", "0002_productimage_productid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimage",
            name="deleted",
            field=models.DateTimeField(blank=True),
        ),
    ]
