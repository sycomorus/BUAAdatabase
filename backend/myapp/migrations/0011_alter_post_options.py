# Generated by Django 5.1.1 on 2024-12-06 06:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0010_notification_myapp_notif_notific_08cde0_idx"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-postDate"]},
        ),
    ]
