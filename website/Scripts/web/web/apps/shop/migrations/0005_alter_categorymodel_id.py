# Generated by Django 4.2.2 on 2023-09-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_goodmodule_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
