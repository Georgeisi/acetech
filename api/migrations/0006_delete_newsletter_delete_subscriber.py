# Generated by Django 4.2.6 on 2023-11-13 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_giftcard'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsletter',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]