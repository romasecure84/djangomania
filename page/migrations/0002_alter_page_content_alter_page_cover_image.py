# Generated by Django 5.0.1 on 2024-01-30 17:21

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("page", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="content",
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="page",
            name="cover_image",
            field=models.ImageField(upload_to="page"),
        ),
    ]
