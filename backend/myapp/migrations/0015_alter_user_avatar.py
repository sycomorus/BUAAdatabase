# Generated by Django 5.1.1 on 2024-12-08 02:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0014_remove_studymaterial_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]