# Generated by Django 3.1 on 2020-08-31 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='Dietary',
        ),
    ]
