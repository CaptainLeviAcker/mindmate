# Generated by Django 4.1.13 on 2024-04-02 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                ("sno", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=200)),
                ("meta", models.CharField(max_length=300)),
                ("content", models.TextField()),
                (
                    "thumbnail_img",
                    models.ImageField(blank=True, null=True, upload_to="images/"),
                ),
                ("thumbnail_url", models.URLField(blank=True, null=True)),
                ("category", models.CharField(default="uncategorized", max_length=255)),
                ("slug", models.CharField(max_length=100)),
                ("time", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
