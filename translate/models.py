from django.db import models
from django.utils import translation


# Create your models here.


class Translate(models.Model):
    key = models.CharField(max_length=255)
    uz = models.TextField()
    ru = models.TextField()
    en = models.TextField()

    def t(key):

        try:
            model = Translate.objects.get(key=key)

            if translation.get_language() == "uz":
                return model.uz
            elif translation.get_language() == "ru":
                return model.ru
            elif translation.get_language() == "en":
                return model.en
        except:
            return key



    def __str__(self):
        return self.key
