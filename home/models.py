from django.db import models



class Home_page_banner(models.Model):
    
    name = models.CharField(max_length=10)
    
    image_banner_1 = models.ImageField(upload_to='photos/banner',blank=True)
    image_banner_2 = models.ImageField(upload_to='photos/banner',blank=True)
    image_banner_3 = models.ImageField(upload_to='photos/banner',blank=True)
    image_banner_4 = models.ImageField(upload_to='photos/banner',blank=True)
    
    def __str__(self) :
        return str(self.name)