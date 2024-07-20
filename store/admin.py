from django.contrib import admin
from .models import Product,Product_appliances,Product_Accesories
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display        = ('product_name' , 'price' , 'stock' , 'category' , 'modified_date', 'is_available')
    prepopulated_fields ={'slug' : ('product_name',)}
    # inlines = [ProductGalleryInline]
    
admin.site.register(Product,ProductAdmin)


class ProductAdmin_appliances(admin.ModelAdmin):
     list_display        = ('product_name' , 'price' , 'stock' , 'category' , 'modified_date', 'is_available')
     prepopulated_fields ={'slug' : ('product_name',)}
    # inlines = [ProductGalleryInline]
    
admin.site.register(Product_appliances,ProductAdmin_appliances)


class ProductAdmin_accesories(admin.ModelAdmin):
     list_display        = ('product_name' , 'price' , 'stock' , 'category' , 'modified_date', 'is_available')
     prepopulated_fields ={'slug' : ('product_name',)}
    # inlines = [ProductGalleryInline]
    
admin.site.register(Product_Accesories,ProductAdmin_accesories)