from django.contrib import admin
from .models import Product,ProductImage,Category,Product_Accessories,Product_Alternative

# Register Your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display        = ['PRDName','PRDSlug','PRDPrice','PRDDiscountPrice','PRDAvaliable','PRDCreated','PRDUpdated']
    list_filter         = ['PRDPrice','PRDAvaliable','PRDCreated','PRDUpdated']
    list_editable       = ['PRDPrice','PRDAvaliable','PRDDiscountPrice']
    prepopulated_fields = {'PRDSlug':('PRDName',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display        = ['CATName','CATSlug']
    prepopulated_fields = {'CATSlug':('CATName',)}


admin.site.register(ProductImage)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)