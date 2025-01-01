# Generated by Django 5.1.3 on 2024-12-11 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 12, 11, 6, 49, 48, 633692, tzinfo=datetime.timezone.utc), verbose_name='Create Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Update Name'),
        ),
    ]