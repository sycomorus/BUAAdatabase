# Generated by Django 5.1.1 on 2024-11-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0003_alter_tutor_rate_alter_tutor_ratenum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tutor",
            name="rate",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="tutor",
            name="rateNum",
            field=models.IntegerField(default=0),
        ),
    ]
