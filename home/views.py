from django.http import HttpResponse
from django.shortcuts import render

from home.forms import ContactForm
from home.models import Setings


# Create your views here.

def index(request):
    context = {"sayfa": "home"}
    return render(request, 'index.html', context)


def contact(request):
    form = ContactForm()
    context = {"sayfa": "Contact - İletişim",
               'form': form}
    return render(request, 'contact.html', context)


def aboutus(request):
    context = {"sayfa": "About Us - Hakkımızda"}
    return render(request, 'aboutus.html', context)


def references(request):
    context = {"sayfa": "References - Referanslar"}
    return render(request, 'references.html', context)
