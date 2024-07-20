# Generated by Django 3.1 on 2024-07-19 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_appliances'),
        ('store', '0003_auto_20240719_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_appliances',
            old_name='created_date_appliances',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='product_appliances',
            old_name='description_appliances',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product_appliances',
            old_name='images_appliances',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='product_appliances',
            old_name='is_available_appliances',
            new_name='is_available',
        ),
        migrations.RenameField(
            model_name='product_appliances',
            old_name='modified_date_appliances',
            new_name='modified_date',
        ),
        migrations.RenameField(
            model_name='product_appliances',
            old_name='price_appliances',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product_appliances',
            old_name='product_name_appliances',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product_appliances',
            old_name='slug_appliances',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='product_appliances',
            old_name='stock_appliances',
            new_name='stock',
        ),
        migrations.RemoveField(
            model_name='product_appliances',
            name='category_appliances',
        ),
        migrations.AddField(
            model_name='product_appliances',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
            preserve_default=False,
        ),
    ]