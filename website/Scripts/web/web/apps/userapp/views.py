# Create your views here.
import re

import django_redis
from django import http
from django.contrib import auth
from django.contrib.auth import login, logout
from django.db import DatabaseError
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views.generic.base import View
from django.shortcuts import render, redirect
from userapp.models import Users
from shop.models import CartModel


class RegisterView(View):

    def get(self, request):
        return render(request, 'userapp/register.html')

    def post(self, request):
        first_name = request.POST.get('name2', '')
        last_name = request.POST.get('username2', '')
        phone = request.POST.get('phone2', '')
        email = request.POST.get('email2', '')
        password = request.POST.get('password2', '')
        confirm_password = request.POST.get('confirm_password', '')
        uuid = request.POST.get('uuid', '')
        remember = request.POST.get('remember')
        email_code = request.POST.get('captcha')
        username = last_name + "-" + first_name
        redis_coon = django_redis.get_redis_connection('verify_code')
        captcha = redis_coon.get('email%s'%uuid).decode('utf-8')
        print(first_name, last_name, phone, email, password, username, confirm_password, email_code)

        if not all([first_name, last_name, phone, email, password, username, confirm_password, email_code]):
            # raise Forbidden('missing required parameter')
            return http.HttpResponseForbidden('missing required parameter')
        if not re.match(r'^[2-9][0-9]{2}[2-9][0-9]{2}[0-9]{4}$', phone):
            return http.HttpResponseForbidden('input right phone number')
            # raise Forbidden('input right phone number')
        if not re.match(r'^([0-9a-zA-Z_-])+@([a-zA-Z0-p_-])+(.[a-zA-Z0-9_-])+', email):
            # raise Forbidden('input right email')
            return http.HttpResponseForbidden('input right email')

        if not re.match(r'^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{8,16}$',password):
            return http.HttpResponseForbidden('input right password')
            # raise Forbidden('input right password')

        if not password == confirm_password:
            raise http.HttpResponseForbidden('The two passwords entered are inconsistent')
        if not email_code == captcha:
            print(email_code, captcha)
            raise http.HttpResponseForbidden('captcha does not match')

        try:
            user = Users.objects.create_user(username=username, first_name=first_name, last_name=last_name, phone=phone,
                                             email=email, password=password)
        except DatabaseError as error:
            print(error)
            return render(request, 'userapp/register.html', {'register_error_message': 'Failed to register'})
        login(request, user)
        if remember != 'on':
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(None)

        return redirect(reverse('homeapp:home'))


class UserNameCheckView(View):
    def get(self,request,username):
        """
        check username
        :param request:
        :param username:
        :return:
        """
        count = Users.objects.filter(username=username).count()

        return JsonResponse({
            'code': 200,
            'error_message': 'OK',
            'count': count,
        })


class LogoutView(View):


    def get(self, request):
        logout(request)
        return redirect(reverse('homeapp:home'))



class PhoneCheckView(View):

    def get(self,request,phone):
        count = Users.objects.filter(phone=phone).count()
        return JsonResponse({
            'code': 200,
            'error_message': 'OK',
            'count': count,
        })




class LoginView(View):

    def get(self,request):

        return render(request, 'userapp/Login.html')

    def post(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        uuid = request.POST.get('uuid')
        img_code = request.POST.get('captcha')
        remember = request.POST.get('remember')
        redis_conn = django_redis.get_redis_connection('verify_code')
        code = redis_conn.get('img%s'%uuid).decode('utf-8')
        print(username,password,uuid,img_code)

        if not all([username,password,uuid,img_code]):
            return http.HttpResponseForbidden('缺少必传参数')

        if not re.match(r'^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).{8,16}$', password):
            return http.HttpResponseForbidden('input right password')
        if code != img_code:
            return http.HttpResponseForbidden('验证码不匹配')

        user = auth.authenticate(username=username, password=password)

        if user is None:
            return http.HttpResponseForbidden('用户名与密码不匹配')

        login(request, user)

        if remember != 'on':
            request.session.set_expiry(0)

        else:
            request.session.set_expiry(None)

        return redirect(reverse('homeapp:home'))


















