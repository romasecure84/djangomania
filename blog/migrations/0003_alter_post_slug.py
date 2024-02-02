# Generated by Django 5.0.1 on 2024-02-02 18:55

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_post_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="title", unique=True
            ),
        ),
    ]
