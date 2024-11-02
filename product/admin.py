from django.contrib import admin
from django.utils.html import format_html

from product.models import Category, Product, Images


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']
    list_display = ['title', 'status']
    list_filter = ['status']
    prepopulated_fields = {"slug": ("title","keywords")}
    readonly_fields = ('image_preview',)
    def image_preview(self, obj):
        """Mevcut resmin önizlemesini gösterir."""
        if obj.image:
            return format_html(
                '<img src="{}" style="max-width: 300px; max-height: 300px;" /><br>'
                '<span>Dosyayı değiştirmek için yeni bir dosya seçin:</span>',
                obj.image.url
            )
        return "Henüz bir resim yüklenmemiş."

    image_preview.short_description = "Yüklü Resim"

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','image_tag','image_preview', 'amount', 'status']
    list_filter = ['status','category']
    readonly_fields = ['image_preview']
    prepopulated_fields = {"slug": ("category","title")}


admin.site.register(Product, ProductAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ['image_tag']

admin.site.register(Images, ImageAdmin)