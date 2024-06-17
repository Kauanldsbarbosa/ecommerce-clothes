# Generated by Django 5.0.6 on 2024-05-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_purchaseorder_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Andress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_street', models.CharField(max_length=120)),
                ('number', models.CharField(max_length=120)),
                ('neighborhood', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
            ],
        ),
    ]