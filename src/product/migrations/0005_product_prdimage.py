# Generated by Django 3.1.2 on 2020-10-11 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20201011_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDImage',
            field=models.ImageField(blank=True, null=True, upload_to='product/', verbose_name='Image'),
        ),
    ]
