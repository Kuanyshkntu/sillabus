# Generated by Django 2.0.2 on 2018-04-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20180421_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lit',
            name='literature_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='literature',
            name='literature_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='takyryp',
            name='number',
            field=models.CharField(default='SOME STRING', max_length=100, unique=True),
        ),
    ]
