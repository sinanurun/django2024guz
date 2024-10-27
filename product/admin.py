from django.contrib import admin

from product.models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title', 'status']
    list_filter = ['status']
    prepopulated_fields = {"slug": ("title","keywords")}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price', 'amount', 'status']
    list_filter = ['status','category']
    # readonly_fields = ['price']
    prepopulated_fields = {"slug": ("category","title")}


admin.site.register(Product, ProductAdmin)