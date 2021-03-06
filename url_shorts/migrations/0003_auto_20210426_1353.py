# Generated by Django 3.2 on 2021-04-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shorts', '0002_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='url',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='urls',
            name='url',
            field=models.TextField(max_length=10000, unique=True),
        ),
        migrations.AlterField(
            model_name='urls',
            name='uuid',
            field=models.TextField(max_length=10, unique=True),
        ),
    ]
