# Generated by Django 2.1.2 on 2019-01-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190108_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smtp', models.CharField(max_length=200, verbose_name='Serwer SMTP')),
                ('sslPort', models.CharField(max_length=200, verbose_name='Port SSL')),
                ('email', models.CharField(max_length=200, verbose_name='Email')),
                ('password', models.CharField(max_length=200, verbose_name='Hasło')),
            ],
            options={
                'verbose_name': 'Konfiguracja serwera email',
                'verbose_name_plural': 'Konfiguracja serwera email',
            },
        ),
        migrations.AlterField(
            model_name='settings',
            name='custom_css',
            field=models.TextField(default='', max_length=10000, verbose_name='Własny CSS (opcja dla zaawansowanych)'),
        ),
    ]
