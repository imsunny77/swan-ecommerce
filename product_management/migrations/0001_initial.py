# Generated by Django 4.0.4 on 2022-04-17 12:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Position')),
                ('display_status', models.IntegerField(choices=[(None, 'SELECT'), (0, 'PUBLISH'), (1, 'DRAFT')], default=0, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(max_length=50, null=True, unique=True, verbose_name='Product Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('position', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Position')),
                ('display_status', models.IntegerField(choices=[(None, 'SELECT'), (0, 'PUBLISH'), (1, 'DRAFT')], default=0, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product_name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.IntegerField(null=True, verbose_name='Available Quantity')),
                ('in_stock', models.IntegerField(blank=True, null=True, verbose_name='In Stock')),
                ('sold', models.IntegerField(blank=True, null=True, verbose_name='Total Sold')),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product_management.productcategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
