from django.shortcuts import render
from django.views.generic import ListView, DetailView
from translations.languages import translate
from .models import *
from main.models import Social, EmailAndPhone

## new lines ##
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import os
import requests
import logging

def asia(request):
    countries = Country.objects.all().translate(translate.ACTIVE)
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
    return render(request, 'asia/asia&sng.html', context)


class UniversityDetailView(DetailView):
    model = University

    def get_context_data(self, **kwargs):
        context = super(UniversityDetailView, self).get_context_data(**kwargs)
        context['emailandphone'] = EmailAndPhone.objects.all()
        context['socials'] = Social.objects.all()
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



## new lines ##
logger = logging.getLogger(__name__)
@csrf_exempt
def form(request):
    if request.method == 'GET':
        return render(request, 'form.html') 
    elif request.method == 'POST':
        try:
            lastname = request.POST.get('lastname')
            name = request.POST.get('name')
            tel_phone = request.POST.get('tel-phone')
            age = request.POST.get('age')
            choosecity = request.POST.get('choosecity')
            certificateselect = request.POST.get('certificateselect')
            message = request.POST.get('message')

            required_fields = [lastname, name, tel_phone, age, choosecity, certificateselect, message]
            if not all(required_fields):
                return JsonResponse({"status": "error", "message": "All fields are required."}, status=400)

            message_text = (
                f"Фамилия: {lastname}\n"
                f"Имя: {name}\n"
                f"Номер телефона: {tel_phone}\n"
                f"Возраст: {age}\n"
                f"Выбранный город: {choosecity}\n"
                f"Есть ли сертификат? {certificateselect}\n"
                f"Сообщение: {message}"
            )

            # Credentials come from the environment (see .env.example), never from the code
            token = os.getenv('TELEGRAM_BOT_TOKEN', '')
            chat_id = os.getenv('TELEGRAM_CHAT_ID', '')
            if not token or not chat_id:
                logger.error("Telegram credentials are not configured (TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID)")
                return JsonResponse({"status": "error", "message": "Failed to send message"}, status=500)
            url = f'https://api.telegram.org/bot{token}/sendMessage'
            payload = {'chat_id': chat_id, 'text': message_text}

            response = requests.post(url, json=payload)

            if response.status_code == 200:
                return JsonResponse({"status": "success", "message": "Message sent successfully"})
            else:
                logger.error(f"Failed to send message: {response.text}")
                return JsonResponse({"status": "error", "message": "Failed to send message"}, status=500)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return JsonResponse({"status": "error", "message": "Internal server error"}, status=500)
    else:
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
