# Generated by Django 5.1.1 on 2024-10-21 01:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0007_recruitmentpost_is_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recruitmentpost",
            name="is_completed",
            field=models.BooleanField(default=True),
        ),
    ]