# Generated by Django 5.1.2 on 2024-10-28 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('duration', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('daily_login_streak', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerBoost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('boost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.boost')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.player')),
            ],
        ),
    ]
