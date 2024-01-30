from django.db import models

# Create your models here.
from django.db.models import Model


class GoodModule(Model):
    name = models.CharField(max_length=50, null=False, blank=False, db_index=True)
    comment = models.TextField(max_length=100, null=True)
    price = models.FloatField(max_length=5, null=False, blank=False)
    user = models.ForeignKey('userapp.Users', null=True, on_delete=models.SET_NULL, related_name='user')
    category = models.ForeignKey('CategoryModel',null=True, on_delete=models.SET_NULL, related_name='category')
    img_url = models.ImageField(null=False,upload_to='type', verbose_name= 'first image')
    status = models.IntegerField(null=True, default=1)
    have = models.IntegerField(default=1)

    class Meta:
        db_table = 't_goods'
        verbose_name = 'Goods'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CategoryModel(Model):
    # id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 't_category'
        verbose_name = 'category'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ImageModel(Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    goods = models.ForeignKey('GoodModule', on_delete=models.CASCADE, related_name='good')
    inner_img = models.ImageField(null=False, verbose_name='inner image')

    class Meta:
        db_table = 't_image'
        verbose_name = 'image'
        verbose_name_plural = verbose_name


class LoveModel(Model):
    user = models.ForeignKey('userapp.Users', on_delete=models.CASCADE, related_name='love', null=True)
    goods_id = models.IntegerField(verbose_name='goods id')
    goods_name = models.CharField(max_length=50, verbose_name='goods name')
    goods_price = models.FloatField(max_length=6, verbose_name='goods price')

    class Meta:
        db_table = 't_love'
        verbose_name = 'love'
        verbose_name_plural = verbose_name


class CartModel(Model):
    user = models.ForeignKey('userapp.Users', on_delete=models.CASCADE, related_name='cart', null=True)
    goods_id = models.IntegerField(verbose_name='goods id')
    goods_name = models.CharField(max_length=50, verbose_name='goods name')
    goods_price = models.FloatField(max_length=6, verbose_name='goods price')

    class Meta:
        db_table = 't_cart'
        verbose_name = 'cart'
        verbose_name_plural = verbose_name


















