# Generated by Django 4.2.3 on 2024-01-27 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_deal_trader_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='system_generated_bilty_number',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]