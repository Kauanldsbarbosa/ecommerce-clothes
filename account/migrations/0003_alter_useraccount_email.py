# Generated by Django 5.0.6 on 2024-06-11 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_useraccount_teste_useraccount_account_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
