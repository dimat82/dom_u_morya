# Generated by Django 2.0.7 on 2018-07-10 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0002_auto_20180709_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100, verbose_name='телефон')),
                ('house', models.ForeignKey(on_delete='', to='houses.House', verbose_name='дом')),
            ],
        ),
    ]
