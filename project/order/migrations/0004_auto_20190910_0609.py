# Generated by Django 2.0 on 2019-09-10 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
