# Generated by Django 4.2.3 on 2024-01-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_deal_dispatched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='fare_paid_by',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
