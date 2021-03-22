from django.contrib import admin
from .models import Product,ProductImage,Category,Product_Accessories,Product_Alternative

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)