# Generated by Django 2.1.4 on 2019-09-03 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20190903_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='round',
            field=models.IntegerField(default=1),
        ),
    ]
