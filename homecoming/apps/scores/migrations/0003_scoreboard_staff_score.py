# Generated by Django 3.1.13 on 2022-02-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scores", "0002_auto_20200715_2206"),
    ]

    operations = [
        migrations.AddField(
            model_name="scoreboard",
            name="staff_score",
            field=models.IntegerField(default=0),
        ),
    ]
