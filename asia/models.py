from django.db import models
from ckeditor.fields import RichTextField
from translations.models import Translatable
from django.utils import translation


# Create your models here.


class Country(Translatable, models.Model):
    name = models.CharField(max_length=100)
    meta_title = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)

    class TranslatableMeta:
        fields = ['name', 'meta_title', 'meta_description', 'meta_keywords']

    def __str__(self):
        return self.name


class University(Translatable, models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='pics')
    name_uz = models.TextField(blank=True, null=True)
    name_ru = models.TextField(blank=True, null=True)
    name_en = models.TextField(blank=True, null=True)
    name_key = models.CharField(max_length=150)
    address_uz = models.CharField(max_length=200, blank=True, null=True)
    address_ru = models.CharField(max_length=200, blank=True, null=True)
    address_en = models.CharField(max_length=200, blank=True, null=True)
    rating = models.IntegerField(null=True, blank=True)
    content_uz = RichTextField(null=True, blank=True)
    content_ru = RichTextField(null=True, blank=True)
    content_en = RichTextField(null=True, blank=True)
    meta_title = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)

    def contentText(self):
        if translation.get_language() == "uz":
            return self.content_uz
        elif translation.get_language() == "ru":
            return self.content_ru
        elif translation.get_language() == "en":
            return self.content_en
        
    def nameText(self):
        if translation.get_language() == "uz":
            return self.name_uz
        elif translation.get_language() == "ru":
            return self.name_ru
        elif translation.get_language() == "en":
            return self.name_en
        
    def addressText(self):
        if translation.get_language() == "uz":
            return self.address_uz
        elif translation.get_language() == "ru":
            return self.address_ru
        elif translation.get_language() == "en":
            return self.address_en

    class TranslatableMeta:
        fields = ['meta_title', 'meta_description', 'meta_keywords']

    def __str__(self):
        return self.name_key
