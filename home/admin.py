from django.contrib import admin

from home.models import Setings, ContactFormMessage

# Register your models here.

admin.site.register(Setings)
admin.site.register(ContactFormMessage)