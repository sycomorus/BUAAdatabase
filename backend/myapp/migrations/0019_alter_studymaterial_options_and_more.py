# Generated by Django 5.1.1 on 2024-12-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_studymaterial_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studymaterial',
            options={'ordering': ['-upload_date']},
        ),
        migrations.AlterField(
            model_name='studymaterial',
            name='upload_date',
            field=models.DateTimeField(),
        ),
    ]
