import os

from alipay import AliPay
from django.conf import settings
from django.core.files.storage import default_storage
from django.db import DataError
from django.http import JsonResponse, HttpResponse

# Create your views here.

import json
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic.base import View
from fdfs_client.client import get_tracker_conf, Fdfs_client
from  shop.models import CategoryModel
from  shop.models import GoodModule

from .models import OrderInfo


class PaymentView(View):

    def post(self, request):
        """
        接受前端的ajax请求
        :param request:
        :return:

        """
        if not request.user.is_authenticated:
            return JsonResponse({'code': 4003, 'error_msg': '用户未登录'})

        param = request.body.decode()

        if not param:
            return JsonResponse({'code': 4001, 'error_msg': '缺少必传信息'})

        param_dir = json.loads(param)
        goods_id = param_dir['goods_id']
        total_count = param_dir['total_count']
        print(total_count)
        pay_method = param_dir['pay_method']
        #创建订单信息
        user = request.user
        order_id = timezone.localtime().strftime('%Y-%m-%d-%H:%M:%S') + str(user.id)
        try:
            order = OrderInfo.objects.create(order_id=order_id,pay_method=pay_method, total_count=total_count,goods_id= goods_id, users=user)
        except DataError:
            return JsonResponse({'code': 4002, 'error_msg': '订单生成失败'})

        #创建alipay对象
        alipay = AliPay(
            appid=settings.APP_ID,
            app_notify_url=None,  # 默认回调 url
            app_private_key_string=settings.APP_PRIVATE_KEY_STRING,
            # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            alipay_public_key_string=settings.ALIPAY_PUBLIC_KEY_STRING,
            sign_type=settings.SIGN,  # RSA 或者 RSA2
            debug=settings.DEBUG,  # 默认 False
        )

        order_str = alipay.api_alipay_trade_page_pay(
            out_trade_no= order_id,
            total_amount=str(order.total_count),
            subject='201-Goodwill%s'%order_id,
            return_url=settings.ALIPAY_RETURN_URL,
            notify_url=settings.ALIPAY_RETURN_URL
        )
        alipay_url = settings.ALIPAY_URL+"?"+order_str
        return JsonResponse({'code': 200, 'error_msg': 'OK', 'alipay_url': alipay_url})


class SellView(View):

    def get(self,request):

        if not request.user.is_authenticated:
            return redirect('/Login/')

        return render(request, 'shop/sell.html')

    def post(self, request):

        goods_name = request.POST.get('TradeName')
        goods_price = request.POST.get('TradePrice')
        goods_type = request.POST.get('TradeTypes').lower()
        goods_quantity = request.POST.get('TradeQuantity')
        goods_comment = request.POST.get('TradeDescription')
        goods_user = request.user
        goods_picture = request.FILES.get('TradePicture')

        image_url = default_storage.save(name=goods_picture.name, content=goods_picture)
        category_have = CategoryModel.objects.filter(name=goods_type).exists()



        # client_conf_object = get_tracker_conf(os.path.join(settings.BASE_DIR, '/utils/fastdfs/client.conf'))
        # client = Fdfs_client(client_conf_object)  # 注意要绝对路径
        # # ret = client.upload_by_buffer(goods_picture.read())
        # try:
        #     result = client.upload_by_buffer(goods_picture.read())
        # except Exception as e:
        #     print(e)
        #     raise
        # if result.get('Status') != 'Upload successed.':
        #     raise Exception('上传文件到FastDFS失败')
        # filename = result.get('Remote file_id')

        print(goods_type)

        if not category_have:
            try:
                category = CategoryModel.objects.create(name=goods_type)
                GoodModule.objects.create(name=goods_name, price=goods_price, comment=goods_comment,
                                          have=goods_quantity, user=goods_user, category=category,
                                          img_url=image_url
                                          )
            except DataError as error:
                print(error)
        else:
            category = CategoryModel.objects.get(name=goods_type)
            GoodModule.objects.create(name=goods_name, price=goods_price, comment=goods_comment,
                                      have=goods_quantity, user=goods_user, category=category,
                                      img_url=image_url
                                      )

        return redirect('/shop/')








