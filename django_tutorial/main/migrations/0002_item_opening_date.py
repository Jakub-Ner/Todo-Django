# Generated by Django 4.1 on 2022-12-12 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="opening_date",
            field=models.CharField(default="NaN", max_length=50),
            preserve_default=False,
        ),
    ]
