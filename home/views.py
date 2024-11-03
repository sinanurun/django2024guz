from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.forms import ContactForm
from home.models import Setings, ContactFormMessage
from product.models import Product


# Create your views here.

def index(request):
    slider = Product.objects.filter(Product.status == 'True').order_by('?')[:4]
    # trandy_product = Product.objects.order_by('viewcount')[:8]
    context = {"sayfa": "home",
               "slider": slider}
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.subject = form.cleaned_data['subject']
            data.ip = request.META['REMOTE_ADDR']
            data.save()
            messages.success(request, 'Mesajınız Başarıyla İletilmiştir')
            return HttpResponseRedirect('/contact')
        else:
            messages.error(request, 'Mesajınız Sisteme Kaydedilmemiştir')
            return HttpResponseRedirect('/contact')
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
