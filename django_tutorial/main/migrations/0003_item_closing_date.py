# Generated by Django 4.1 on 2022-12-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_item_opening_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="closing_date",
            field=models.DateTimeField(null=True),
        ),
    ]
