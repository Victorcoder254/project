# Generated by Django 5.1.4 on 2025-01-03 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appzinara', '0004_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
