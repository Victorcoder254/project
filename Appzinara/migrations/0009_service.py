# Generated by Django 5.1.4 on 2025-01-03 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appzinara', '0008_rename_is_closed_operatinghours_operates_public_holidays_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.DurationField(help_text='Duration of the service (e.g., 00:30:00 for 30 minutes)')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='Appzinara.business')),
            ],
        ),
    ]
