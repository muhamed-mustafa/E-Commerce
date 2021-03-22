# Generated by Django 3.1.2 on 2020-10-10 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=100, verbose_name='Product Name')),
                ('PRDDesc', models.TextField(verbose_name='Product Description')),
                ('PRDPrice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price')),
                ('PRDCost', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Cost')),
                ('PRDCreated', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDIImage', models.ImageField(upload_to='product/', verbose_name='Image')),
                ('PRDIProduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Product')),
            ],
        ),
    ]