from django.shortcuts import render

from .models import *

from translations.languages import translate

from main.models import Comment, Social, EmailAndPhone

# Create your views here.


def about(request):
    maintext = MainText.objects.all().translate(translate.ACTIVE)
    checkmarktext = CheckMarkText.objects.all().translate(translate.ACTIVE)
    othertext = OtherText.objects.all().translate(translate.ACTIVE)
    ourteam = OurTeam.objects.all().translate(translate.ACTIVE)
    feature = Feature.objects.all().translate(translate.ACTIVE)
    emailandphone = EmailAndPhone.objects.all()
    socials = Social.objects.all()
    context = {
        'maintext': maintext,
        'checkmarktext': checkmarktext,
        'othertext': othertext,
        'ourteam': ourteam,
        'features': feature,
        'emailandphone': emailandphone,
        'socials': socials,

    }
    return render(request, 'about.html', context)


def testimonials(request):
    comment = Comment.objects.all().translate(translate.ACTIVE)
    emailandphone = EmailAndPhone.objects.all()
    socials = Social.objects.all()
    titleString = ""
    descriptionString = ""
    keywordsString = ""
    for com in comment:
        titleString += str(com.meta_title)
        descriptionString += str(com.meta_description)
        keywordsString += str(com.meta_keywords)
    context = {
        'comments': comment,
        'emailandphone': emailandphone,
        'socials': socials,
        'titleString': titleString,
        'descriptionString': descriptionString,
        'keywordsString': keywordsString
    }
    return render(request, 'testimonials.html', context)


def faq(request):
    faq = Faq.objects.all().translate(translate.ACTIVE)
    emailandphone = EmailAndPhone.objects.all()
    socials = Social.objects.all()
    titleString = ""
    descriptionString = ""
    keywordsString = ""
    for fa in faq:
        titleString += str(fa.meta_title)
        descriptionString += str(fa.meta_description)
        keywordsString += str(fa.meta_keywords)
    context = {
        'faqs': faq,
        'emailandphone': emailandphone,
        'socials': socials,
        'titleString': titleString,
        'descriptionString': descriptionString,
        'keywordsString': keywordsString
    }
    return render(request, 'faq.html', context)
