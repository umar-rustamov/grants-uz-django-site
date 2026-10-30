from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from translations.languages import translate
from django.utils import translation
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings

from .models import *


def setlanguage(request, lang):
    if lang in dict(settings.LANGUAGES):
        translation.activate(lang)
        request.session['lang'] = lang
    referer = request.META.get('HTTP_REFERER')
    if referer and url_has_allowed_host_and_scheme(referer, allowed_hosts={request.get_host()}):
        return HttpResponseRedirect(referer)
    return redirect('/')


def index(request):
    emailandphone = EmailAndPhone.objects.all()
    socials = Social.objects.all()
    sidebar_socials = Sidebar_Social.objects.all()
    # translate.ACTIVE = 'uz'
    # translation.activate('uz')
    headercarousel = HeaderCarousel.objects.all().translate(translate.ACTIVE)
    purpose = Purpose.objects.all().translate(translate.ACTIVE)
    advantage = Advantage.objects.all().translate(translate.ACTIVE)
    countries_img = CountriesImage.objects.all()
    result = OurResult.objects.all()
    rec_univ = RecommendedUniversity.objects.all()
    comment = Comment.objects.all().translate(translate.ACTIVE)
    context = {
        'emailandphone': emailandphone,
        'socials': socials,
        'headercarousel': headercarousel,
        'purposes': purpose,
        'advantages': advantage,
        'countries': countries_img,
        'results': result,
        'recommendeds': rec_univ,
        'comments': comment,
        'sidebar_socials': sidebar_socials

    }
    return render(request, 'index.html', context)
