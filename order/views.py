import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from order.models import AddFavorite
from product.models import Product

favori_list = []
# Create your views here.
@login_required(login_url='/user/login')
def addfavorite(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    product = Product.objects.get(pk = id)
    checkinproduct = AddFavorite.objects.filter(product_id = id, user_id = current_user.id) # True False

    if checkinproduct:
        messages.success(request, 'Ürün Zaten Favorilerde Mevcut')
        return HttpResponseRedirect(url)
    else:
        data = AddFavorite()
        data.product_id = id
        data.user_id = current_user.id
        data.save()
        favori_list.append(data.id)
        json_data = json.dumps(favori_list)
        request.session['favori_list'] = json_data
        # request.session['favori_list_len'] = len(favori_list)
        request.session['favori_items'] = AddFavorite.objects.filter(user_id = current_user.id).count()
        messages.success(request, 'Ürün favorilere eklendi')
        return HttpResponseRedirect(url)



@login_required(login_url='/user/login')
def favorites(request):
    current_user = request.user
    favorites = AddFavorite.objects.filter(user=current_user)
    context = {'favorites':favorites}
    return render(request, 'favorites_products.html',context)