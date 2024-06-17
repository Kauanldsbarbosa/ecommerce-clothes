# Generated by Django 5.0.6 on 2024-05-25 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_status',
            field=models.CharField(blank=True, choices=[('P', 'Pendente'), ('A', 'Aceito'), ('S', 'Enviado'), ('E', 'Entregue')], max_length=1),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='total',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
