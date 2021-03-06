# Generated by Django 2.1.5 on 2019-01-08 16:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20190108_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Temat')),
                ('text', models.CharField(max_length=20000, verbose_name='Zawartość')),
                ('created_date', models.TextField(default=django.utils.timezone.now, verbose_name='Data wysłania')),
            ],
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data zapisania'),
        ),
    ]
