# Generated by Django 3.2.5 on 2021-07-23 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxonomy',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='term',
            name='description',
            field=models.TextField(default='', null=True),
        ),
    ]