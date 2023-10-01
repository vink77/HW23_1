from django.contrib import admin
from catalog.models import Category, Product
# Register your models here.
#admin.site.register(Category)

#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'price', 'category', 'avatar')
    list_filter = ('category',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name',)
    list_filter = ('category_name',)