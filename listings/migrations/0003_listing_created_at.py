# Generated by Django 3.2.5 on 2021-07-22 10:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_rename_listings_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
