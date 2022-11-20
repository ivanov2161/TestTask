from django.shortcuts import render
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def home(request):
    return render(request, 'home.html')
