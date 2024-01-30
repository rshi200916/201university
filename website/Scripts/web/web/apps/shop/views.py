from django import http
from django.db import DataError
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View
from shop.models import CategoryModel
from shop.models import GoodModule
from shop.models import CartModel
from shop.models import LoveModel


class ShoppView(View):
    def get(self, request):
        try:
            goods = GoodModule.objects.all().order_by('id')
        except GoodModule.DoesNotExist:
            return http.HttpResponseForbidden('no goods')

        return render(request, 'shop/change_shop.html', {'goods': goods})


class LoveView(View):

    def get(self, request):

        if not request.user.is_authenticated:

            return redirect('/Login/')

        user = request.user

        kinds = LoveModel.objects.filter(user=user).order_by('id')
        good_id_list = [good.goods_id for good in kinds if good]
        goods = GoodModule.objects.filter(id__in=good_id_list).order_by('id')

        return render(request, 'shop/love.html', {'goods':goods})


class CartView(View):

    def get(self, request):

        if not request.user.is_authenticated:

            return redirect('/Login/')
        user = request.user
        kinds = CartModel.objects.filter(user=user).order_by('id')

        good_id_list = [good.goods_id for good in kinds if good]

        goods = GoodModule.objects.filter(id__in=good_id_list).order_by('id')

        return render(request, 'shop/cart.html', {'goods': goods})


class KindView(View):

    def get(self, request, kind):

        try:
            kinds = CategoryModel.objects.get(name=kind)
        except CategoryModel.DoesNotExist:
            return http.HttpResponseForbidden('no find this kind shop')
        category = kinds.category.all()
        goods_id_list = [goods.id for goods in category if goods]
        goods = GoodModule.objects.filter(id__in=goods_id_list).order_by('id')
        print(goods)
        return render(request, '/shop/test.html', {'goods': goods})


class MiddleView(View):
    def get(self,request, good_id):
        try:
            good = GoodModule.objects.get(id=good_id)
        except GoodModule.DoesNotExist:
            return http.HttpResponseForbidden('no goods')

        return render(request, '/shop/home_shop.html', {'good':good})


class AddCartView(View):
    def get(self,request,good_id):
        if not request.user.is_authenticated:
            return redirect('/Login/')
        user = request.user
        good = GoodModule.objects.get(id=good_id)
        num = CartModel.objects.filter(Q(user=user) & Q(goods_id=good_id)).count()
        print(num)
        if num != 0:
            return redirect('/shop/')
        try:
            CartModel.objects.create(user=user, goods_id=good.id, goods_name=good.name, goods_price=good.price)
        except DataError:
            return JsonResponse({'code':404,'error_message':'adding to shopping cart failed'})
        return redirect('/shop/')


class AddLoveView(View):

    def get(self, request, good_id):

        if not request.user.is_authenticated:
            return redirect('/Login/')
        user = request.user
        good = GoodModule.objects.get(id=good_id)
        num = LoveModel.objects.filter(Q(user=user) & Q(goods_id=good_id)).count()
        print(num)
        if num != 0:
            return redirect('/shop/')
        try:
            LoveModel.objects.create(user=user, goods_id=good.id, goods_name=good.name, goods_price=good.price)
        except DataError:
            return JsonResponse({'code': 404, 'error_message': 'adding to shopping cart failed'})
        return redirect('/shop/')


class CartRemoveView(View):
    def get(self, request, user_id, good_id):
        try:
            CartModel.objects.filter(user_id=user_id, goods_id=good_id).delete()
        except DataError:
            return JsonResponse({'code': 4001, 'error_message': 'delete failed'})
        return redirect('/shop/cart')


class LoveRemoveView(View):
    def get(self, request, user_id, good_id):
        try:
            LoveModel.objects.filter(user_id=user_id, goods_id=good_id).delete()
        except DataError:
            return JsonResponse({'code': 4001, 'error_message': 'delete failed'})
        return redirect('/shop/love')





