# Generated by Django 2.0.2 on 2018-03-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20180306_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.Subject'),
        ),
        migrations.AlterField(
            model_name='literature',
            name='god',
            field=models.DateField(blank=True, null=True),
        ),
    ]
