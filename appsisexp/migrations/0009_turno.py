# Generated by Django 3.0.5 on 2023-01-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsisexp', '0008_pruebas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_turno', models.DateField()),
                ('Hora_turno', models.CharField(max_length=10)),
                ('Nro_celular', models.CharField(max_length=11, null=True)),
                ('Nombre', models.CharField(max_length=80, null=True)),
                ('Tema', models.CharField(max_length=150, null=True)),
                ('Monto_consulta', models.DecimalField(decimal_places=2, max_digits=9)),
                ('Onservacion', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]