# Generated by Django 2.2.3 on 2019-08-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20190804_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=75, unique=True),
        ),
    ]
