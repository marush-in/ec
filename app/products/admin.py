from django.contrib import admin
from django.db import models
from django.forms import TextInput
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Brand, Product, PopularProduct


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category_image',)
    list_editable = ['name', 'slug']


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'brand_image')
    list_editable = ['name', 'slug']


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
    list_display = (
        'id', 'name', 'slug', 'category', 'brand', 'is_published',
    )
    list_display_links = ['name']
    list_editable = ['is_published']
    list_per_page = 20
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(PopularProduct)
