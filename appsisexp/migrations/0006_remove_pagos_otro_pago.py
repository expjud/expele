# Generated by Django 3.0.5 on 2023-01-03 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsisexp', '0005_auto_20230103_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagos',
            name='otro_pago',
        ),
    ]