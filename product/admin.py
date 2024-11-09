from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import DraggableMPTTAdmin

from product.models import Category, Product, Images, Comment


# resim galerisi oluşturmak için inline yapı
class ProductImagesInline(admin.TabularInline):
    model = Images
    extra = 5
    readonly_fields = ('image_tag',)

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

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Category, CategoryAdmin2)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','image_tag','image_preview', 'amount', 'status']
    list_filter = ['status','category']
    readonly_fields = ['image_preview']
    inlines = [ProductImagesInline]
    prepopulated_fields = {"slug": ("category","title")}


admin.site.register(Product, ProductAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image_tag']
    readonly_fields = ['image_tag',]

admin.site.register(Images, ImageAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_filter = ('status',)
admin.site.register(Comment, CommentAdmin)