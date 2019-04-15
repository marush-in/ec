from django.contrib import admin
from .models import Category, Brand, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'updated_at')
    list_editable = ['name', 'slug']


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'updated_at')
    list_editable = ['name', 'slug']


class ProductAdmin(admin.ModelAdmin):
    summernote_fields = ('description',)
    list_display = (
        'id', 'name', 'slug', 'category', 'brand', 'is_published',
    )
    list_editable = ['is_published']
    list_per_page = 20


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
