from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from product.forms import SearchForm, CommentForm
from product.models import Category, Product, Images


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
    images = Images.objects.filter(product_id = id)
    urunKategori = Category.objects.get(pk=urun.category_id)
    kategoriurunleri = Product.objects.filter(category_id=urun.category_id)
    form = CommentForm
    context = {'urun':urun,'images':images,
               'urunKategori':urunKategori,
               'kategoriurunleri':kategoriurunleri, 'form':form}
    return render(request,'product_detail.html',context)

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(title__icontains=query)
            context = {'results':results}
            return render(request, 'product_search.html', context)
    return HttpResponseRedirect('/')