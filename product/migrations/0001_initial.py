# Generated by Django 5.0.6 on 2024-05-25 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='no product name', max_length=150)),
                ('description', models.CharField(blank=True, max_length=2080)),
                ('price', models.FloatField(default=0.0)),
                ('promotional_price', models.FloatField(blank=True, default=0.0)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, choices=[('p', 'pequeno'), ('m', 'medio'), ('g', 'grande'), ('gg', 'extra grande'), ('xg', 'extra extra grande'), ('xgg', 'extra extra grande')], max_length=3)),
                ('color', models.CharField(blank=True, choices=[('az', 'azul'), ('am', 'amarelo'), ('bra', 'branco'), ('vrd', 'verde'), ('vrm', 'vermelho'), ('ma', 'marrom'), ('ci', 'cinza'), ('pr', 'preto')], max_length=3)),
                ('price', models.FloatField(default=0.0)),
                ('promotional_price', models.FloatField(blank=True, default=0.0)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('stock', models.IntegerField(blank=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
            ],
        ),
    ]
