# Generated by Django 2.0 on 2019-09-09 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='image1',
            field=models.TextField(),
        ),
    ]
