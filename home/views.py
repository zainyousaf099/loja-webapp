from django.shortcuts import render
from home.models import Home_page_banner
# Create your views here.
def home(request):
    
    banner_image = Home_page_banner.objects.all()
    
    context ={
        "banner_image": banner_image
    }
    return render(request, 'home.html',context)