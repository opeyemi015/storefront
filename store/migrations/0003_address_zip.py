# Generated by Django 4.0.2 on 2022-02-12 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.PositiveIntegerField(default='00000'),
            preserve_default=False,
        ),
    ]
