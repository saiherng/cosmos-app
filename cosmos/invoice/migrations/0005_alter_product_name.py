# Generated by Django 4.0.2 on 2022-03-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_cart_alter_invoice_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(choices=[('Sakura', 'Sakura'), ('Romance', 'Romance'), ('Juicy', 'Juicy'), ('Intricate', 'Intricate'), ('Destiny', 'Destiny'), ('Honey', 'Honey'), ('Pl', 'Pl'), ('Floral', 'Floral')], max_length=20),
        ),
    ]
