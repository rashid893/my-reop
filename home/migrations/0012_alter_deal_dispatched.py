# Generated by Django 4.2.3 on 2024-01-29 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_deal_system_generated_bilty_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='dispatched',
            field=models.CharField(max_length=255),
        ),
    ]
