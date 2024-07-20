from django.contrib import admin
from .models import Category,Category_appliances,Category_Accessories


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields     =   {'slug':('category_name',)}
    list_display            =   ('category_name','slug')
    
admin.site.register(Category,CategoryAdmin)

class CategoryAdmin_appliances(admin.ModelAdmin):
    prepopulated_fields     =   {'slug':('category_name',)}
    list_display            =   ('category_name','slug')
    
admin.site.register(Category_appliances,CategoryAdmin_appliances)


class CategoryAdmin_accesories(admin.ModelAdmin):
    prepopulated_fields     =   {'slug':('category_name',)}
    list_display            =   ('category_name','slug')
    
admin.site.register(Category_Accessories,CategoryAdmin_accesories)