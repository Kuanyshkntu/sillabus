# Generated by Django 2.0.2 on 2018-04-21 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_lit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lit',
            name='god',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='literature',
            name='god',
            field=models.DateField(blank=True, null=True),
        ),
    ]