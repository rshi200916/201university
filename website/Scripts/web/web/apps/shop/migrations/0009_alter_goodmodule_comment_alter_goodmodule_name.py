# Generated by Django 4.2.2 on 2023-09-02 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_cartmodel_user_alter_lovemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodmodule',
            name='comment',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='goodmodule',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
