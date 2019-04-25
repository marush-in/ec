from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, PopularPost


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 6, 'cols': 100})},
    }
    list_display = (
        'id', 'title', 'slug', 'is_published', 'admin_eyecatch', 'created_at',
    )
    list_display_links = ['title']
    list_editable = ['is_published']
    list_per_page = 20


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'created_at', 'updated_at')
    list_editable = ['name', 'slug']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PopularPost)
