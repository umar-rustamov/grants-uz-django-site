from django.db import models
from asia.models import University as University_asia
from europa.models import University as University_europa
from oceania.models import University as University_oceania

from translations.models import Translatable


# Create your models here.

class EmailAndPhone(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)

class Social(models.Model):
    telegram_link = models.TextField()
    facebook_link = models.TextField()
    instagram_link = models.TextField()
    email = models.EmailField()
    tiktok_link = models.TextField()


class Socials(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Sidebar_Social(models.Model):
    which_social_media = models.OneToOneField(Socials, on_delete=models.CASCADE)
    link = models.TextField()

    def __str__(self):
        return self.which_social_media.name


class HeaderCarousel(Translatable, models.Model):
    active = models.BooleanField()
    country = models.CharField(max_length=150)
    content = models.TextField()
    bg_img = models.ImageField(upload_to='pics')

    class TranslatableMeta:
        fields = ['country', 'content']


class Purpose(Translatable, models.Model):
    content = models.TextField()
    advantage_img = models.ImageField(upload_to='pics')

    class TranslatableMeta:
        fields = ['content']


class Advantage(Translatable, models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()

    class TranslatableMeta:
        fields = ['title', 'content']


class CountriesImage(models.Model):
    asia_img = models.ImageField(upload_to='pics')
    europe_img = models.ImageField(upload_to='pics')
    oceania_img = models.ImageField(upload_to='pics')


class OurResult(models.Model):
    count_student = models.IntegerField()
    count_university = models.IntegerField()
    count_grant = models.IntegerField()
    count_preparation_course = models.IntegerField()


class RecommendedUniversity(models.Model):
    logo_img = models.ImageField(upload_to='pics')
    which_university_asia = models.ForeignKey(University_asia, on_delete=models.CASCADE, blank=True, null=True)
    which_university_europa = models.ForeignKey(University_europa, on_delete=models.CASCADE, blank=True, null=True)
    which_university_oceania = models.ForeignKey(University_oceania, on_delete=models.CASCADE, blank=True, null=True)

    # if which_university_asia:
    #     def __str__(self):
    #         return self.which_university_asia.name
    # elif which_university_europa:
    #     def __str__(self):
    #         return self.which_university_europa.name
    # elif which_university_europa:
    #     def __str__(self):
    #         return self.which_university_europa.name


class Comment(Translatable, models.Model):
    user_img = models.ImageField(upload_to='pics')
    username = models.CharField(max_length=70)
    where_studies = models.CharField(max_length=150)
    comment = models.TextField()
    meta_title = models.TextField(blank=True)
    meta_description = models.TextField(blank=True)
    meta_keywords = models.TextField(blank=True)

    class TranslatableMeta:
        fields = ['username', 'where_studies', 'comment', 'meta_title', 'meta_description', 'meta_keywords']

