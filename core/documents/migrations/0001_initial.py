# Generated by Django 4.1.7 on 2023-06-18 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('providers', '0001_initial'),
        ('tax_machine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_doc', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Document type',
                'verbose_name_plural': 'Documents type',
            },
        ),
        migrations.CreateModel(
            name='RetIVA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro_ret', models.CharField(blank=True, max_length=30, null=True)),
                ('date_reception', models.DateField(blank=True, null=True)),
                ('date_ret_iva', models.DateField(blank=True, null=True)),
                ('amount_iva', models.FloatField(blank=True, null=True)),
                ('percent_iva', models.FloatField(blank=True, null=True)),
                ('amount_ret_iva', models.FloatField(blank=True, null=True)),
                ('purchasebonate_accountant', models.CharField(blank=True, max_length=20, null=True)),
                ('purchasebonate_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Retention IVA',
                'verbose_name_plural': 'Retentions IVA',
            },
        ),
        migrations.CreateModel(
            name='SaleSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('n_invoice', models.CharField(max_length=20)),
                ('zeta', models.CharField(max_length=20)),
                ('since', models.DateField()),
                ('until', models.DateField()),
                ('machine', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='tax_machine.taxmachine')),
            ],
            options={
                'verbose_name': 'Sale summary',
                'verbose_name_plural': 'Sales summaries',
            },
        ),
        migrations.CreateModel(
            name='SaleDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=20)),
                ('document_number', models.CharField(max_length=20)),
                ('ctrl_number', models.CharField(max_length=20)),
                ('issuance_date', models.DateField()),
                ('registration_date', models.DateField()),
                ('type_record', models.CharField(choices=[('1', 'Registro'), ('2', 'Complemeto'), ('3', 'Anulación'), ('4', 'Ajuste')], max_length=20)),
                ('customer_code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='customers.customer')),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='documents.documenttype')),
            ],
            options={
                'verbose_name': 'Sale document',
                'verbose_name_plural': 'Sale documents',
            },
        ),
        migrations.CreateModel(
            name='PurchaseDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=20)),
                ('document_number', models.CharField(max_length=20)),
                ('ctrl_number', models.CharField(max_length=20)),
                ('issuance_date', models.DateField(max_length=20)),
                ('registration_date', models.DateField()),
                ('type_record', models.CharField(choices=[('1', 'Registro'), ('2', 'Complemeto'), ('3', 'Anulación'), ('4', 'Ajuste')], max_length=20)),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='documents.documenttype')),
                ('provider_code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='providers.provider')),
            ],
            options={
                'verbose_name': 'Purchase document',
                'verbose_name_plural': 'Purchasing documents',
            },
        ),
        migrations.CreateModel(
            name='ItemDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.FloatField()),
                ('iva', models.FloatField()),
                ('amount_iva', models.FloatField()),
                ('c_ctrl', models.FloatField(blank=True, null=True)),
                ('patente', models.FloatField(blank=True, null=True)),
                ('ret', models.FloatField(blank=True, null=True)),
                ('purchase_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.purchasedocument')),
                ('sale_document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.saledocument')),
            ],
            options={
                'verbose_name': 'Item document',
                'verbose_name_plural': 'Items documents',
            },
        ),
    ]
