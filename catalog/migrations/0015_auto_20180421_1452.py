# Generated by Django 2.0.2 on 2018-04-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20180421_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='takyryp',
            name='takyryp_aty',
            field=models.CharField(max_length=100),
        ),
    ]