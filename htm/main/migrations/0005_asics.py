# Generated by Django 4.1.5 on 2023-05-26 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cryptocoin_hashrate_no_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('hashrate_no_code', models.CharField(max_length=60)),
            ],
        ),
    ]
