from django.contrib import admin

from .models import Category, SubCategory, VendorPost, Brand, FeaturedProducts
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(VendorPost)
admin.site.register(Brand)
admin.site.register(FeaturedProducts)

