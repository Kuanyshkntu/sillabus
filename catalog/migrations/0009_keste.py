# Generated by Django 2.0.2 on 2018-04-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20180403_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apta', models.CharField(max_length=100)),
                ('lekcia', models.CharField(max_length=100)),
                ('zert', models.CharField(max_length=100)),
            ],
        ),
    ]
