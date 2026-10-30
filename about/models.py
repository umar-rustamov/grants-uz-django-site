from django.db import models
from translations.models import Translatable


# Create your models here.

class MainText(Translatable, models.Model):
    main_text = models.TextField()
    second_text = models.TextField()

    class TranslatableMeta:
        fields = ['main_text', 'second_text']


class CheckMarkText(Translatable, models.Model):
    text = models.TextField()

    class TranslatableMeta:
        fields = ['text']


class OtherText(Translatable, models.Model):
    text_1 = models.TextField()
    text_2 = models.TextField(blank=True)
    text_3 = models.TextField(blank=True)
    text_4 = models.TextField(blank=True)
    text_5 = models.TextField(blank=True)

    class TranslatableMeta:
        fields = ['text_1', 'text_2', 'text_3', 'text_4', 'text_5']


class OurTeam(Translatable, models.Model):
    img = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=70)
    career = models.CharField(max_length=100)
    what_work = models.TextField(blank=True)

    class TranslatableMeta:
        fields = ['name', 'career', 'what_work']


class Feature(Translatable, models.Model):
    activates = models.BooleanField()
    main_title = models.CharField(max_length=150)
    title = models.TextField()
    italic_text = models.TextField()
    text = models.TextField()
    img_sidebar = models.ImageField(upload_to='pics')

    class TranslatableMeta:
        fields = ['main_title', 'title', 'italic_text', 'text']


class Faq(Translatable, models.Model):
    activates = models.BooleanField()
    title = models.TextField()
    text = models.TextField()
    meta_title = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)

    class TranslatableMeta:
        fields = ['title', 'text', 'meta_title', 'meta_description', 'meta_keywords']
