# Generated by Django 2.0 on 2019-09-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_cart_single_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.BooleanField(default=False),
        ),
    ]
