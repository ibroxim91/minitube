# Generated by Django 5.0.1 on 2024-01-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocontent',
            name='views',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
