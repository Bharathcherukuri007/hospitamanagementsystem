# Generated by Django 3.1.7 on 2021-05-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0027_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='images',
            field=models.ImageField(upload_to='cart/'),
        ),
    ]
