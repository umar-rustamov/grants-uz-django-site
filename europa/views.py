from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *

from main.models import Social, EmailAndPhone


def europa(request):
    countries = Country.objects.all()
    universities = University.objects.all()
    emailandphone = EmailAndPhone.objects.all()
    socials = Social.objects.all()
    titleString = ""
    descriptionString = ""
    keywordsString = ""
    for fa in countries:
        titleString += str(fa.meta_title)
        descriptionString += str(fa.meta_description)
        keywordsString += str(fa.meta_keywords)
    context = {
        'countries': countries,
        'universities': universities,
        'emailandphone': emailandphone,
        'socials': socials,
        'titleString': titleString,
        'descriptionString': descriptionString,
        'keywordsString': keywordsString
    }
    return render(request, 'europa/europe.html', context)


class UniversityDetailView(DetailView):
    model = University

    def get_context_data(self, **kwargs):
        context = super(UniversityDetailView, self).get_context_data(**kwargs)
        context['socials'] = Social.objects.all()
        context['emailandphone'] = EmailAndPhone.objects.all()
        titleString = ""
        descriptionString = ""
        keywordsString = ""
        universities = University.objects.all()
        for fa in universities:
            titleString += str(fa.meta_title)
            descriptionString += str(fa.meta_description)
            keywordsString += str(fa.meta_keywords)

        context['titleString'] = titleString
        context['descriptionString'] = descriptionString
        context['keywordsString'] = keywordsString
        return context
