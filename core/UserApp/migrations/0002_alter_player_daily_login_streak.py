# Generated by Django 5.1.2 on 2024-10-28 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='daily_login_streak',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
