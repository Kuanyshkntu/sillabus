# Generated by Django 2.0.2 on 2018-04-25 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20180425_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='literature',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='takyryp',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='subject',
        ),
        migrations.AddField(
            model_name='literature',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Subject'),
        ),
        migrations.AddField(
            model_name='takyryp',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Subject'),
        ),
    ]
