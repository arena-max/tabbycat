# Generated by Django 2.1.3 on 2019-01-14 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0008_auto_20181224_1719'),
        ('notifications', '0009_auto_20181126_1001'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SentMessageRecord',
            new_name='SentMessage',
        ),
    ]