# Generated by Django 3.1 on 2020-08-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200828_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavour', models.CharField(max_length=250)),
                ('Dietary', models.CharField(max_length=250)),
            ],
        ),
    ]
