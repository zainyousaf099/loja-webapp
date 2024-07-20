from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('appliances/', views.store_appliances, name='appliances'),
    path('accesories/', views.store_accesories, name='accesories'),
    path('category/<slug:category_slug>/', views.store, name='product_by_category'),
    path('appliances/<slug:category_slug>/', views.store_appliances, name='product_by_category_appliances'),
    path('accesories/<slug:category_slug>/', views.store_accesories, name='product_by_category_accesories'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_details, name='product_details'),
    path('accesories/<slug:category_slug>/<slug:product_slug>/', views.product_details_accesories, name='product_details_accesories'),
    path('appliances/<slug:category_slug>/<slug:product_slug>/', views.product_details_appliances, name='product_appliances'),

]
