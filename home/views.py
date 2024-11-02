
from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setings


# Create your views here.

def index(request):
    settings = Setings.objects.get(pk=1)
    metin = "BTK Kursiyerleri"
    # return HttpResponse("Hello, %s. <br>You're at the" % metin)
    # return HttpResponse(metin)
    context = {"sayfa":"home",
               'settings':settings}

    # return render(request, 'index.html',context)
    return render(request, 'index.html', context)