# Generated by Django 5.1.1 on 2024-12-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0012_studymaterial_file_user_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.CharField(
                blank=True,
                default="http://120.46.1.4:9000/zxb/png/Akkarin.png",
                max_length=255,
                null=True,
            ),
        ),
    ]
