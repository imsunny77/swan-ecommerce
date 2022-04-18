# Generated by Django 4.0.4 on 2022-04-18 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_alter_rootuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='address_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='address_1',
            field=models.CharField(max_length=50, null=True, verbose_name='Address Line 1'),
        ),
    ]