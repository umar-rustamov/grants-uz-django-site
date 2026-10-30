from django import template
from translate.models import Translate
from main.models import EmailAndPhone, Social

register = template.Library()


# All custom template tag go here

@register.simple_tag
def t(key):
    # Your method definition
    return Translate.t(key)


@register.simple_tag
def site_contact():
    # Phone and email for the header/footer, so every page has them
    return EmailAndPhone.objects.first()


@register.simple_tag
def site_social():
    return Social.objects.first()
