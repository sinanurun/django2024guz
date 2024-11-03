from django.http import HttpResponse
from django.shortcuts import render

from product.models import Category, Product


# Create your views here.

def index(request):
    return HttpResponse("urunler")

def categoryProducts(request,id, slug):
    urunKategori = Category.objects.get(pk = id)
    urunler = Product.objects.filter(category_id = id)
    context = {'urunler':urunler,
               'urunKategori':urunKategori}
    return render(request,'kategori_urunler.html',context)