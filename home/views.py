from django.http import HttpResponse
from django.shortcuts import render

from home.forms import ContactForm
from home.models import Setings


# Create your views here.

def index(request):
    settings = Setings.objects.get(pk=1)
    metin = "BTK Kursiyerleri"
    # return HttpResponse("Hello, %s. <br>You're at the" % metin)
    # return HttpResponse(metin)
    context = {"sayfa": "home",
               'settings': settings}
    return render(request, 'index.html', context)


def contact(request):
    settings = Setings.objects.get(pk=1)
    metin = "BTK Kursiyerleri"
    # return HttpResponse("Hello, %s. <br>You're at the" % metin)
    # return HttpResponse(metin)
    form = ContactForm()
    context = {"sayfa": "Contact - İletişim",
               'settings': settings,
               'form':form}
    return render(request, 'contact.html', context)


def aboutus(request):
    settings = Setings.objects.get(pk=1)
    metin = "BTK Kursiyerleri"
    # return HttpResponse("Hello, %s. <br>You're at the" % metin)
    # return HttpResponse(metin)
    context = {"sayfa": "About Us - Hakkımızda",
               'settings': settings}
    return render(request, 'aboutus.html', context)


def references(request):
    settings = Setings.objects.get(pk=1)
    metin = "BTK Kursiyerleri"
    context = {"sayfa": "References - Referanslar",
               'settings': settings}
    return render(request, 'references.html', context)
