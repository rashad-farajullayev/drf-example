# Generated by Django 3.2 on 2021-04-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=2000)),
                ('ean', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('prod_date', models.DateField()),
                ('exp_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]