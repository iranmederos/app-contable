# Generated by Django 4.1.7 on 2023-04-06 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buysdocument',
            name='items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='documents.documentsitems'),
        ),
        migrations.AddField(
            model_name='salesdocument',
            name='items',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='documents.documentsitems'),
        ),
    ]
