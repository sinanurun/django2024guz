"""
URL configuration for django2024guz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django2024guz import settings
from django.contrib import admin
from django.urls import path, include


from home import views as homeviews
from product import views as prductviews
urlpatterns = ([
    path('admin/', admin.site.urls),
    # uygulama pathleri
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('api/', include('productapi.urls')),
    path('search/', prductviews.search, name='search'),
    path('product/<int:id>/<slug:slug>/', prductviews.productDetail, name='productDetail'),
    path('category/<int:id>/<slug:slug>/', prductviews.categoryProducts, name='categoryProducts' ),
    # path('product/', include('product.urls')),
    # anasayfalar
    path('', homeviews.index, name='index'),
    path('contact', homeviews.contact, name='contact'),
    path('aboutus', homeviews.aboutus, name='aboutus'),
    path('references', homeviews.references, name='references'),
    # eklenti pathleri
    path('ckeditor/', include('ckeditor_uploader.urls')),
]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
