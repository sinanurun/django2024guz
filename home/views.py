from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):

    metin = "BTK Kursiyerleri"
    # return HttpResponse("Hello, %s. <br>You're at the" % metin)
    # return HttpResponse(metin)
    context = {"icerik1":metin}
    # return render(request, 'index.html',context)
    return render(request, 'index.html')