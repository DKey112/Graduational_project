# Generated by Django 4.1.5 on 2023-04-25 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("gamenews", "0004_alter_post_post_pic"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="game",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to="gamenews.game",
                verbose_name="Discipline ",
            ),
        ),
    ]
