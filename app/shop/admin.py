from django.contrib import admin
from django.db import models
from django.forms import TextInput
from django_summernote.admin import SummernoteModelAdmin

from .models import (
    Settings,
    Guide,
    Privacy_policy,
    Company,
    Faq,
    Legal,
    Faq_content
)


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name')


class GuideAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }


class Privacy_policyAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }


class CompanyAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }


class FaqAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')


class LegalAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
    }


class Faq_contentAdmin(SummernoteModelAdmin):
    list_display = ('id', 'question',)
    list_per_page = 20


admin.site.register(Settings, SettingsAdmin)
admin.site.register(Guide, GuideAdmin)
admin.site.register(Privacy_policy, Privacy_policyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Legal, LegalAdmin)
admin.site.register(Faq_content, Faq_contentAdmin)