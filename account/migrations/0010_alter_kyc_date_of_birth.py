# Generated by Django 5.0.1 on 2024-07-18 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_alter_kyc_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kyc',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
    ]
