# Generated by Django 5.1.1 on 2024-10-30 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpost",
            name="published",
        ),
        migrations.AddField(
            model_name="blogpost",
            name="is_published",
            field=models.BooleanField(default=False, verbose_name="Уже тут"),
        ),
    ]
