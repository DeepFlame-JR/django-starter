# Generated by Django 4.1.7 on 2023-04-06 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("third", "0002_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="Restaurant",
            new_name="restaurant",
        ),
    ]
