# Generated by Django 2.0 on 2019-08-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_investmentmodel_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='investmentmodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
