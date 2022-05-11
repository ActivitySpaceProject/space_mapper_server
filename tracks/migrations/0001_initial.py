# Generated by Django 4.0.4 on 2022-05-11 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedIPs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IP_address', models.GenericIPAddressField()),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'allowed IP address',
                'verbose_name_plural': 'allowed IP addresses',
            },
        ),
        migrations.CreateModel(
            name='DataPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_UUID', models.CharField(max_length=36)),
                ('user_code', models.CharField(max_length=8)),
                ('app_version', models.CharField(blank=True, max_length=300, null=True)),
                ('type', models.CharField(max_length=3)),
                ('encrypted_message', models.TextField()),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'data point',
                'verbose_name_plural': 'data points',
            },
        ),
    ]
