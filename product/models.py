from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.

class Category(models.Model):
    STATUS = (('True', 'Evet'),('False', 'Hayir'))
    title = models.CharField(max_length=30, verbose_name='Başlık')
    keywords = models.CharField(blank=True, max_length=250, verbose_name='Anahtar Kelimeler')
    description = models.CharField(blank=True, max_length=250)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.title

class Product(models.Model):
    STATUS=( ('True','Evet'),('False','Hayir'))
    category=models.ForeignKey(Category,on_delete=models.CASCADE)#manytoonerelationwithCategory
    title=models.CharField(max_length=150)
    keywords=models.CharField(blank=True,max_length=255)
    description=models.TextField(blank=True,max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    #price=models.DecimalField(max_digits=12,decimal_places=2,default=0)
    price=models.FloatField()
    amount=models.IntegerField(default=0)
    # detail=RichTextUploadingField()
    detail=models.TextField()
    status=models.CharField(max_length=10,choices=STATUS,default='False')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    slug=models.SlugField(null=False,unique=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    def image_tag(self):
        return mark_safe('<img src="{}" width="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

    def __str__(self):
        return self.title