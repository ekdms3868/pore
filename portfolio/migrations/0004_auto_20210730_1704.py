# Generated by Django 3.0.6 on 2021-07-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_business'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='pf_attach',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
