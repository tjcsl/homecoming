# Generated by Django 3.1.13 on 2022-02-28 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0003_scoreboard_staff_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreboard',
            name='staff_score',
        ),
    ]
