# Generated by Django 5.0.1 on 2024-08-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_status',
            field=models.CharField(choices=[('failed', 'failed'), ('completed', 'completed'), ('failed', 'failed'), ('pending', 'pending'), ('processing', 'processing'), ('requested', 'requested'), ('request_processing', 'request_processing'), ('none', 'none')], default='pending', max_length=100),
        ),
    ]
