# Generated by Django 5.0.6 on 2024-06-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_cartitem_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
