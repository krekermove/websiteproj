# Generated by Django 4.1.7 on 2023-06-04 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='lattitude',
            field=models.FloatField(default=0, verbose_name='Широта'),
        ),
        migrations.AddField(
            model_name='places',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='Долгота'),
        ),
    ]
