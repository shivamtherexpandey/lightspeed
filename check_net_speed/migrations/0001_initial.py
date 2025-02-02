# Generated by Django 4.2 on 2024-06-25 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserInternetSpeed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("download_speed", models.FloatField()),
                ("upload_speed", models.FloatField()),
                ("latency", models.IntegerField()),
            ],
        ),
    ]
