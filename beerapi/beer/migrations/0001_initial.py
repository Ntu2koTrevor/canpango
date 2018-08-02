# Generated by Django 2.0.1 on 2018-08-02 08:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BeerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('style', models.CharField(default='', max_length=254)),
                ('ibu', models.IntegerField(default='')),
                ('calories', models.IntegerField(default='')),
                ('abv', models.IntegerField(default='')),
                ('location', models.CharField(default='', max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Beers',
            },
        ),
        migrations.CreateModel(
            name='RateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aroma', models.PositiveIntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default='5')),
                ('appearance', models.PositiveIntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default='5')),
                ('taste', models.PositiveIntegerField(choices=[(10, 10), (9, 9), (8, 8), (7, 7), (6, 6), (5, 5), (4, 4), (3, 3), (2, 2), (1, 1)], default='10')),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.BeerModel')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
