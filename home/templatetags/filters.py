from django.template.defaulttags import register
from django import template

register = template.Library()


# Getting a dictianory's key filter
@register.filter
def get_key_value(dictionary, key):
    return dictionary.get(key)
