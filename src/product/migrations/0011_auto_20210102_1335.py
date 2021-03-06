# Generated by Django 3.1.2 on 2021-01-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20201014_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='CATSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Category Slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(blank=True, null=True, verbose_name='Product Slug'),
        ),
    ]
