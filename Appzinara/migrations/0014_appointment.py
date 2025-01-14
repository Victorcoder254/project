# Generated by Django 5.1.4 on 2025-01-07 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appzinara', '0013_alter_business_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('customer_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('customer_gender', models.CharField(blank=True, max_length=10, null=True)),
                ('customer_date_of_birth', models.DateField(blank=True, null=True)),
                ('appointment_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='Appzinara.business')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='Appzinara.service')),
            ],
        ),
    ]
