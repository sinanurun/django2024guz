from order.models import AddFavorite, ShopCart


def favori_sorgusu(request):
    if request.user.is_authenticated:
        request.session['favori_items'] = (
            AddFavorite.objects.filter(user_id=request.user.id).count())
        request.session['cart_items'] = ShopCart.objects.filter(user_id=request.user.id).count()

        return {'favori_itemss': request.session['favori_items'],'cart_items':request.session['cart_items']}
    else:
        request.session['favori_items'] = 0
        request.session['cart_items'] = 0
        return {'favori_itemss': request.session['favori_items'],'cart_items':request.session['cart_items']}