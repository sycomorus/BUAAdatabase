# Generated by Django 5.1.1 on 2024-12-08 02:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0013_alter_user_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="studymaterial",
            name="file",
        ),
    ]
