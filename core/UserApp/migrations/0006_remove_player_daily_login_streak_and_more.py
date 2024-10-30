# Generated by Django 5.1.2 on 2024-10-28 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0005_level_prize_playerlevel_levelprize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='daily_login_streak',
        ),
        migrations.RemoveField(
            model_name='player',
            name='username',
        ),
        migrations.AddField(
            model_name='player',
            name='player_id',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]