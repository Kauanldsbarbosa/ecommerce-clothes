# Generated by Django 5.0.6 on 2024-05-25 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_purchaseorder_order_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]