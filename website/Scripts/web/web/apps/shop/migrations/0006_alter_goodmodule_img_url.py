# Generated by Django 4.2.2 on 2023-09-01 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_categorymodel_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodmodule',
            name='img_url',
            field=models.ImageField(upload_to='type', verbose_name='first image'),
        ),
    ]
