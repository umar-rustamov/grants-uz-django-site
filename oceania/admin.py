from django.contrib import admin
from translations.admin import TranslatableAdmin, TranslationInline
from .models import *


# Register your models here.


class ContinentAdmin(TranslatableAdmin):
    inlines = [TranslationInline]


admin.site.register(Country, ContinentAdmin)
admin.site.register(University, ContinentAdmin)
