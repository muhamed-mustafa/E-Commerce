# Generated by Django 3.1.2 on 2020-10-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product_prdslug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDDiscountPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Discount Price'),
        ),
    ]
