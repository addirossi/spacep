from django.contrib import admin

from product.models import Category, Product, ProductImage


#TODO: Реализовать загрузку нескольких изображений
class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    list_filter = ['category']
    search_fields = ['name', 'description']
    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
