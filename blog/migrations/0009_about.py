# Generated by Django 2.1.2 on 2019-01-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_settings_custom_css'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(default='', max_length=200000, verbose_name='O autorze')),
            ],
            options={
                'verbose_name': 'O autorze',
                'verbose_name_plural': 'O autorze',
            },
        ),
    ]
