# Generated by Django 2.0 on 2019-09-04 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20190904_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createprofie',
            name='active',
        ),
    ]
