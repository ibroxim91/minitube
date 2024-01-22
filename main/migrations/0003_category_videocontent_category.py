# Generated by Django 5.0.1 on 2024-01-19 12:30

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_videocontent_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='videocontent',
            name='category',
            field=models.ForeignKey( on_delete=django.db.models.deletion.PROTECT, related_name='videos', to='main.category'),
            preserve_default=False,
        ),
    ]
