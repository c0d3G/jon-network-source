# Generated by Django 2.2.3 on 2019-09-14 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_chat_time_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='channel',
            field=models.CharField(default='', max_length=100),
        ),
    ]