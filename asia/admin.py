from django.contrib import admin
from translations.admin import TranslatableAdmin, TranslationInline
from .models import Country, University
# from django import forms
# from ckeditor.widgets import CKEditorWidget


# class UniversityAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#
#     class Meta:
#         model = University
#
#
# class UniversityAdmin(TranslatableAdmin):
#     form = UniversityAdminForm


# Register your models here.


class ContinentAdmin(TranslatableAdmin):
    inlines = [TranslationInline]


admin.site.register(Country, ContinentAdmin)
admin.site.register(University, ContinentAdmin)
