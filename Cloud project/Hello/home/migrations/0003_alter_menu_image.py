# Generated by Django 4.2.1 on 2023-07-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_remove_tables_image_remove_tables_layout"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="menu_images/"),
        ),
    ]
