# Generated by Django 4.1.5 on 2023-05-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gamenews", "0008_player_game"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="post_amount",
            field=models.IntegerField(default=0),
        ),
    ]
