# Generated by Django 4.2.2 on 2023-08-29 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodmodule',
            name='have',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='goodmodule',
            name='status',
            field=models.IntegerField(default=1, null=True),
        ),
    ]