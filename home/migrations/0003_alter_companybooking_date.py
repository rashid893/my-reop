# Generated by Django 4.2.3 on 2024-01-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_products_bank_payment_slip_number_companybooking_bank_payment_slip_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybooking',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]