# Generated by Django 4.1.7 on 2023-04-06 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='type_sales',
            field=models.CharField(choices=[('1', 'Interna'), ('2', 'Exportacion')], max_length=20),
        ),
    ]