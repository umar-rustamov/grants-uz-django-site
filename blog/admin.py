from django.contrib import admin
from translations.admin import TranslatableAdmin, TranslationInline
from .models import *


# Register your models here.


class ContinentAdmin(TranslatableAdmin):
    inlines = [TranslationInline]


admin.site.register(Blog, ContinentAdmin)
admin.site.register(Recent)
admin.site.register(Tag)
admin.site.register(PicturesGallery)
admin.site.register(Filial, ContinentAdmin)