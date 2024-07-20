from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):

    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

    class Meta:

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_urls(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return str(self.category_name)


class Category_appliances(models.Model):

    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)

    class Meta:

        verbose_name = 'category_appliances'
        verbose_name_plural = 'categories_appliances'

    def get_urls(self):
        return reverse('product_by_category_appliances', args=[self.slug] )
    
    def __str__(self):
        return str(self.category_name)
    
class Category_Accessories(models.Model):

    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cat_image = models.ImageField(upload_to='photos/categories/', blank=True)
    
    class Meta:

        verbose_name = 'category_Accessories'
        verbose_name_plural = 'categories_Accessories'

    def get_urls(self):
        return reverse('products_by_category_accesories', args=[self.slug] )
    
    def __str__(self):
        return str(self.category_name)
