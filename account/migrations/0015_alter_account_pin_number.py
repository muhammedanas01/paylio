# Generated by Django 5.0.1 on 2024-08-15 19:44

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_account_pin_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pin_number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=4, max_length=4, prefix=''),
        ),
    ]
