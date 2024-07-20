from django.db import models
from django.urls import reverse
from category.models import Category,Category_appliances,Category_Accessories
# Create your models here.


class Product(models.Model):

    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    
    def get_url(self):
        
        return reverse('product_details', args = [self.category.slug , self.slug])

    def __str__(self):
        return str(self.product_name)


class Product_appliances(models.Model):

    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category_appliances, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    def get_url_appliances(self):
        
        return reverse('product_appliances', args = [self.category.slug , self.slug])
    
   

    def __str__(self):
        return str(self.product_name)
    
    
    
class Product_Accesories(models.Model):

    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category_Accessories, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
   
    def get_url_accesories(self):
        
        return reverse('product_details_accesories', args = [self.category.slug , self.slug])
    
    def __str__(self):
        return str(self.product_name)
