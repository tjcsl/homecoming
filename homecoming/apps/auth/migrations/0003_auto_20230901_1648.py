# Generated by Django 3.1.13 on 2023-09-01 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0002_auto_20201107_1851"),
    ]

    operations = [
        migrations.CreateModel(
            name="ClassGroup",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("username_prefix", models.CharField(max_length=4)),
                ("message", models.TextField(blank=True, max_length=48000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="is_class_group_admin",
            field=models.BooleanField(default=False),
        ),
    ]
