from django.contrib import admin
from .models import Product, Offer

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'description')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)