# Generated by Django 3.0 on 2020-06-30 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('l10n_cuba', '0003_populate_table_municipio'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoPostal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_postal', models.PositiveIntegerField(verbose_name='Código Postal')),
                ('localidad', models.CharField(blank=True, max_length=150, null=True, verbose_name='Localidad')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codigos_postales', to='l10n_cuba.Municipio')),
            ],
            options={
                'verbose_name': 'Código Postal',
                'verbose_name_plural': 'Códigos Postales',
            },
        ),
    ]
