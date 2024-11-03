from .models import Setings
def settings(request):
    settings = Setings.objects.get(pk=1)
    # return {'settings': Setings.objects.get(pk=1)}
    if settings:
        return {'settings': settings}