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

def productDetail(request,id, slug):
    urun = Product.objects.get(id=id)
    urun.viewcount = urun.viewcount + 1
    urun.save()
    urunKategori = Category.objects.get(pk=urun.category_id)
    kategoriurunleri = Product.objects.filter(category_id=urun.category_id)
    context = {'urun':urun,
               'urunKategori':urunKategori,
               'kategoriurunleri':kategoriurunleri}
    return render(request,'product_detail.html',context)