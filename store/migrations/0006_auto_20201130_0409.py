# Generated by Django 3.1.3 on 2020-11-30 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('1', 'Cameras'), ('2', 'Accessories'), ('3', 'New Arrivals')], max_length=1),
        ),
    ]
