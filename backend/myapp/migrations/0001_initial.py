# Generated by Django 5.1.1 on 2024-10-24 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.IntegerField(blank=True, null=True)),
                ("gender", models.IntegerField(blank=True, null=True)),
                ("contact", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                ("grade", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tutor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.IntegerField(blank=True, null=True)),
                ("gender", models.IntegerField(blank=True, null=True)),
                ("contact", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.EmailField(blank=True, max_length=255, null=True)),
                ("rating", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("identity", models.IntegerField()),
                ("registration_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="StudentPost",
            fields=[
                ("post_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("postDate", models.DateTimeField(blank=True, null=True)),
                ("startDate", models.DateField(blank=True, null=True)),
                ("endDate", models.DateField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "fullLocation",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "telephoneNumber",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "emailAddress",
                    models.EmailField(blank=True, max_length=255, null=True),
                ),
                ("content", models.TextField(blank=True, null=True)),
                ("is_completed", models.BooleanField()),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.student"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentPostSubject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "studentPost_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.studentpost",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudyMaterial",
            fields=[
                ("material_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("upload_date", models.DateField()),
                ("content", models.TextField()),
                (
                    "receiver_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.student"
                    ),
                ),
                (
                    "uploader_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.tutor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StudentNotification",
            fields=[
                (
                    "studentNotification_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("notificationDate", models.DateTimeField(blank=True, null=True)),
                ("content", models.TextField(blank=True, null=True)),
                ("is_read", models.BooleanField()),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.student"
                    ),
                ),
                (
                    "tutor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.tutor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("review_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("rating", models.IntegerField()),
                ("content", models.TextField()),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.student"
                    ),
                ),
                (
                    "tutor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.tutor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TutorNotification",
            fields=[
                (
                    "tutorNotification_id",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("notificationDate", models.DateTimeField(blank=True, null=True)),
                ("content", models.TextField(blank=True, null=True)),
                ("is_read", models.BooleanField()),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.student"
                    ),
                ),
                (
                    "tutor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.tutor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TutorPost",
            fields=[
                ("post_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("postDate", models.DateTimeField(blank=True, null=True)),
                ("startDate", models.DateField(blank=True, null=True)),
                ("endDate", models.DateField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "fullLocation",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "telephoneNumber",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "emailAddress",
                    models.EmailField(blank=True, max_length=255, null=True),
                ),
                ("content", models.TextField(blank=True, null=True)),
                ("is_completed", models.BooleanField()),
                (
                    "tutor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.tutor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TutorPostSubject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "tutorPost_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.tutorpost",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="tutor",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
            ),
        ),
    ]
