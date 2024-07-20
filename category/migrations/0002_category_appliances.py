# Generated by Django 3.1 on 2024-07-19 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_appliances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name_appliances', models.CharField(max_length=50, unique=True)),
                ('slug_appliances', models.SlugField(max_length=100, unique=True)),
                ('description_appliances', models.TextField(blank=True, max_length=255)),
                ('cat_image_appliances', models.ImageField(blank=True, upload_to='photos/categories/')),
            ],
            options={
                'verbose_name': 'category_appliances',
                'verbose_name_plural': 'categories_appliances',
            },
        ),
    ]