# Generated by Django 4.1.7 on 2023-12-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0002_vendor_credits_bills_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_credits_bills',
            name='shipping_charge',
            field=models.FloatField(blank=True, null=True),
        ),
    ]