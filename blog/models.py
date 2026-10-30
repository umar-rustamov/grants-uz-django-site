from django.db import models
from translations.models import Translatable


# Create your models here.

class Blog(Translatable, models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.TextField()
    text = models.TextField()
    blog_main_detail_text = models.TextField()
    author_name = models.CharField(max_length=100)
    date_posted = models.CharField(max_length=50)
    count_comments = models.CharField(max_length=50)
    main_phrase = models.TextField(blank=True)
    detail_title_1 = models.TextField(blank=True)
    detail_text_1 = models.TextField(blank=True)
    detail_img_1 = models.ImageField(upload_to='pics', blank=True)
    detail_title_2 = models.TextField(blank=True)
    detail_text_2 = models.TextField(blank=True)
    detail_img_2 = models.ImageField(upload_to='pics', blank=True)
    detail_title_3 = models.TextField(blank=True)
    detail_text_3 = models.TextField(blank=True)
    detail_img_3 = models.ImageField(upload_to='pics', blank=True)
    meta_title = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)

    class TranslatableMeta:
        fields = [
            'title', 'text', 'blog_main_detail_text', 'author_name',
            'main_phrase', 'detail_title_1', 'detail_text_1', 'detail_img_1',
            'detail_title_2', 'detail_text_2', 'detail_img_2',
            'detail_title_3', 'detail_text_3', 'detail_img_3',
            'meta_title', 'meta_description', 'meta_keywords'
        ]

    def __str__(self):
        return self.author_name


class Recent(models.Model):
    which_blog = models.ForeignKey(Blog, on_delete=models.CASCADE)


class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class PicturesGallery(models.Model):
    img = models.ImageField(upload_to='pics')


class Filial(Translatable, models.Model):
    title = models.CharField(max_length=150)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20, blank=True)
    third_phone = models.CharField(max_length=20, blank=True)
    location_link_https = models.TextField()
    meta_title = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)

    class TranslatableMeta:
        fields = ['title', 'address', 'meta_title', 'meta_description', 'meta_keywords']

    def __str__(self):
        return self.title
