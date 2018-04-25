# Generated by Django 2.0.2 on 2018-04-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20180419_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('literature_name', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('izdanie', models.CharField(blank=True, max_length=100)),
                ('stranica', models.CharField(blank=True, max_length=100)),
                ('god', models.DateField(blank=True, default='', null=True)),
                ('typee', models.CharField(blank=True, choices=[('Н', 'Негізгі'), ('Қ', 'Қосымша')], default='m', help_text='Book availability', max_length=1)),
            ],
        ),
    ]
