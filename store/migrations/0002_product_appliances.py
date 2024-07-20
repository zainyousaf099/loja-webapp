# Generated by Django 3.1 on 2024-07-19 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_appliances'),
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_appliances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name_appliances', models.CharField(max_length=200, unique=True)),
                ('slug_appliances', models.SlugField(max_length=200, unique=True)),
                ('description_appliances', models.TextField(blank=True, max_length=500)),
                ('price_appliances', models.IntegerField()),
                ('images_appliances', models.ImageField(upload_to='photos/products')),
                ('stock_appliances', models.IntegerField()),
                ('is_available_appliances', models.BooleanField(default=True)),
                ('created_date_appliances', models.DateTimeField(auto_now_add=True)),
                ('modified_date_appliances', models.DateTimeField(auto_now=True)),
                ('category_appliances', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
