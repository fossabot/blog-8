# Generated by Django 2.1.2 on 2019-01-07 10:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190107_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]