# Generated by Django 4.1.7 on 2023-04-13 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_options_alter_company_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='registrationdata',
            options={'verbose_name': 'Registration date', 'verbose_name_plural': 'Registration date'},
        ),
    ]