# Generated by Django 3.1.7 on 2022-03-12 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_merge_0005_alter_product_name_0005_auto_20220312_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
