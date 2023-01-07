# Generated by Django 3.0.5 on 2023-01-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsisexp', '0004_auto_20230103_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='Observacion',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='pagos',
            name='otro_pago',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagos',
            name='Monto_acordado',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='pagos',
            name='Pago_parcial',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]