# Generated by Django 3.1 on 2024-07-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home_page_banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('image_banner_1', models.ImageField(blank=True, upload_to='photos/banner')),
                ('image_banner_2', models.ImageField(blank=True, upload_to='photos/banner')),
                ('image_banner_3', models.ImageField(blank=True, upload_to='photos/banner')),
                ('image_banner_4', models.ImageField(blank=True, upload_to='photos/banner')),
            ],
        ),
    ]