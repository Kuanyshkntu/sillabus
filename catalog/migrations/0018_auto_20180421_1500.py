# Generated by Django 2.0.2 on 2018-04-21 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_auto_20180421_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takyryp',
            name='number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]