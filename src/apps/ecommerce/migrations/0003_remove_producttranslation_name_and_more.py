# Generated by Django 5.0.7 on 2024-07-13 14:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ecommerce", "0002_translations"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="producttranslation",
            name="name",
        ),
        migrations.RemoveField(
            model_name="producttranslation",
            name="slug",
        ),
        migrations.AddField(
            model_name="product",
            name="name",
            field=models.CharField(
                db_index=True, default=django.utils.timezone.now, max_length=200
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="slug",
            field=models.SlugField(
                default=django.utils.timezone.now, max_length=200, unique=True
            ),
            preserve_default=False,
        ),
    ]
