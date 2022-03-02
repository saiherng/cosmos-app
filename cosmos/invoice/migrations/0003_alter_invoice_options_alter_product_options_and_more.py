# Generated by Django 4.0.2 on 2022-03-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_alter_customer_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'ordering': ['customer']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='items',
            field=models.ManyToManyField(to='invoice.Product'),
        ),
    ]