# Generated by Django 3.0.5 on 2021-10-31 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appsisexp', '0002_auto_20211008_2359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expedien',
            name='Audiencia_exp',
        ),
        migrations.RemoveField(
            model_name='expedien',
            name='Cliente_exp',
        ),
        migrations.RemoveField(
            model_name='expedien',
            name='Documental_exp',
        ),
        migrations.RemoveField(
            model_name='expedien',
            name='Evento_exp',
        ),
        migrations.RemoveField(
            model_name='expedien',
            name='Pagos_exp',
        ),
        migrations.RemoveField(
            model_name='expedien',
            name='Tramite_exp',
        ),
        migrations.AddField(
            model_name='audiencia',
            name='Audiencia_exp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appsisexp.Expedien'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Cliente_exp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appsisexp.Expedien'),
        ),
        migrations.AddField(
            model_name='documental',
            name='Documental_exp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appsisexp.Expedien'),
        ),
        migrations.AddField(
            model_name='evento',
            name='Evento_exp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appsisexp.Expedien'),
        ),
        migrations.AddField(
            model_name='pagos',
            name='Pagos_exp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appsisexp.Expedien'),
        ),
        migrations.AddField(
            model_name='tramite',
            name='Tramite_exp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appsisexp.Expedien'),
        ),
    ]
