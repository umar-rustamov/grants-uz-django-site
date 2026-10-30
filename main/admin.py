from django.contrib import admin
from translations.admin import TranslatableAdmin, TranslationInline
from .models import *


# Register your models here.


class ContinentAdmin(TranslatableAdmin):
    inlines = [TranslationInline]


admin.site.register(EmailAndPhone)
admin.site.register(Social)
admin.site.register(HeaderCarousel, ContinentAdmin)
admin.site.register(Purpose, ContinentAdmin)
admin.site.register(Advantage, ContinentAdmin)
admin.site.register(CountriesImage)
admin.site.register(OurResult)
admin.site.register(RecommendedUniversity)
admin.site.register(Comment, ContinentAdmin)
admin.site.register(Socials)
admin.site.register(Sidebar_Social)

