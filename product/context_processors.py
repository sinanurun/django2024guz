from product.models import Category


def categories(request):
    # categories = Category.objects.filter(parent=None, status='True')
    categories = Category.objects.all()
    if categories :
        return {'categories': categories}
    else:
        return dict()