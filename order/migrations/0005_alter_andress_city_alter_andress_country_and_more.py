# Generated by Django 5.0.6 on 2024-05-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_andress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='andress',
            name='city',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='andress',
            name='country',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='andress',
            name='name_street',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='andress',
            name='neighborhood',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='andress',
            name='number',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='andress',
            name='state',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
