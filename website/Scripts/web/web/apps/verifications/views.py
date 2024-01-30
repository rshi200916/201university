import string
from random import random

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
# from captcha.image import ImageCaptcha
import django_redis
from verifications.send import send_email_code
from celery_tasks.tasks import send_sms

from web.apps.verifications.send import *

# Create your views here.



class ImageCodeView(View):
    def get(self,request,uuid):
        seed = string.digits
        r = random.choices(seed, k=6)
        img_code_str = ''.join(r)
        # img_code = ImageCaptcha.generate_image(chars=img_code_str)
        redis_conn = django_redis.get_redis_connection('verify_code')
        # redis_conn.setex('img_%s'%uuid, 120,img_code_str)
        #便于验证码的频繁调用（多个用户）pipeline为管道应用
        pl = redis_conn.pipeline()
        pl.setex('img%s'%uuid, 60,img_code_str)
        pl.execute()
        return HttpResponse(img_code_str)


class EmailVerify(View):
    def get(self, request, uuid):
        email = request.GET.get('email')
        print(email)
        # codes = send_sms(email)

        codes = send_email_code(email)
        print(codes)

        if codes:
            redis_conn = django_redis.get_redis_connection('verify_code')
            pl = redis_conn.pipeline()
            pl.setex('email%s' % uuid, 60, codes)
            print('email%s' % uuid)
            pl.execute()
            return JsonResponse({
                'status': "Ok",
                'code': 200,
                'error_message': '',

            })
        else:
            return JsonResponse({
                'status': 'No',
                'code': 200,
                'error_message': '发送失败，请确保您的Email正确',

                 })














