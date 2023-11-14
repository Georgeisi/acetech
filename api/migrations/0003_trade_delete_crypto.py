# Generated by Django 4.2.6 on 2023-11-11 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_subscriber_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(max_length=50)),
                ('rate', models.BigIntegerField()),
                ('min', models.BigIntegerField()),
                ('Max', models.BigIntegerField()),
                ('variant', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Crypto',
        ),
    ]
