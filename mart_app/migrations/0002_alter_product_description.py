# Generated by Django 5.0.2 on 2024-03-10 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mart_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
