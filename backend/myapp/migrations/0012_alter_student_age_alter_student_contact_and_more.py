# Generated by Django 5.1.1 on 2024-10-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0011_rename_user_id_jobpost_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="contact",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="gender",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="grade",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="tutor",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="tutor",
            name="contact",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="tutor",
            name="gender",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="tutor",
            name="grade",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="tutor",
            name="rating",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
