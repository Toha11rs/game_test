# Generated by Django 5.1.2 on 2024-10-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_alter_player_daily_login_streak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
