# Generated by Django 4.1.7 on 2023-06-18 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constitution_date', models.DateField()),
                ('registration_date', models.DateField()),
                ('registration_number', models.CharField(max_length=50, unique=True)),
                ('registration_office', models.CharField(max_length=50)),
                ('registration_city', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Registration date',
                'verbose_name_plural': 'Registration date',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('business_name', models.CharField(max_length=50, unique=True)),
                ('fiscal_period_ini', models.DateField()),
                ('fiscal_period_end', models.DateField()),
                ('rif', models.CharField(max_length=20, unique=True)),
                ('rif_second', models.CharField(max_length=20, unique=True)),
                ('ret_iva', models.FloatField(blank=True)),
                ('tax_residence', models.CharField(max_length=100)),
                ('number_phone', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=20, unique=True)),
                ('domiciled', models.BooleanField()),
                ('nacionality', models.CharField(choices=[('1', 'Nacional'), ('2', 'Extranjero')], max_length=20)),
                ('exempt_income', models.BooleanField()),
                ('economic_denomination', models.CharField(max_length=20)),
                ('type_person', models.CharField(choices=[('1', 'Natural'), ('2', 'Juridica')], max_length=20)),
                ('type_taxpayer', models.CharField(choices=[('1', 'Formal'), ('2', 'Ordinario'), ('3', 'Especial'), ('4', 'Publico'), ('5', 'No Especial')], max_length=20)),
                ('registration_data', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='company.registrationdata')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
    ]
