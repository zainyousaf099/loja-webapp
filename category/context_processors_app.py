from .models import Category_appliances

def menu_links(request):
    links = Category_appliances.objects.all()
    return dict(links=links)
    