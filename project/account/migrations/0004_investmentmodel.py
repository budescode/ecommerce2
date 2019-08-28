# Generated by Django 2.0 on 2019-08-01 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_auto_20190801_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(choices=[('BASIC PACKAGE 30% DAILY', 'BASIC PACKAGE 30% DAILY'), ('BUSINESS PACKAGE 15% DAILY', 'BUSINESS PACKAGE 15% DAILY'), ('PROFESSIONAL PACKAGE 20% DAILY', 'PROFESSIONAL PACKAGE 20% DAILY')], max_length=1000)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
