from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from . import views


urlpatterns =[
    re_path('^shop/payment/$', views.PaymentView.as_view()),
    re_path('^shop/sell/$', views.SellView.as_view()),
]