from django.contrib import admin
from translations.admin import TranslatableAdmin, TranslationInline
from .models import *


# Register your models here.


class ContinentAdmin(TranslatableAdmin):
    inlines = [TranslationInline]


admin.site.register(MainText, ContinentAdmin)
admin.site.register(CheckMarkText, ContinentAdmin)
admin.site.register(OtherText, ContinentAdmin)
admin.site.register(OurTeam, ContinentAdmin)
admin.site.register(Feature, ContinentAdmin)
admin.site.register(Faq, ContinentAdmin)