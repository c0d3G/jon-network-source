# Generated by Django 2.2.3 on 2019-09-30 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_reply_md_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='md_body',
        ),
        migrations.AlterField(
            model_name='reply',
            name='body',
            field=models.TextField(),
        ),
    ]