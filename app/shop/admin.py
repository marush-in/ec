from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django_summernote.admin import SummernoteModelAdmin

from .models import (
    Settings,
    Guide,
    Privacy_policy,
    Company,
    Terms_of_use,
    Faq,
    Legal,
    Faq_content
)


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'site_name')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'cols': 100})},
    }


class GuideAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }


class PrivacyPolicyAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }


class CompanyAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }


class TermsOfUseAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }


class FaqAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }


class LegalAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title')
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }


class FaqContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'question',)
    list_per_page = 20
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '100'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 4, 'cols': 100})},
    }


admin.site.register(Settings, SettingsAdmin)
admin.site.register(Guide, GuideAdmin)
admin.site.register(Privacy_policy, PrivacyPolicyAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Terms_of_use, TermsOfUseAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Legal, LegalAdmin)
admin.site.register(Faq_content, FaqContentAdmin)
