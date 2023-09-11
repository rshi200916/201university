
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path('^shop/$', views.ShoppView.as_view(), name='shop'),
    re_path('^shop/love/$', views.LoveView.as_view()),
    re_path('^shop/cart/$', views.CartView.as_view()),
    re_path('^shop/kind/(?P<kind>[a-zA-Z]{3,15})/$', views.KindView.as_view()),
    re_path('^shop/page/(?P<good_id>[0-9]+)/$', views.MiddleView.as_view()),
    re_path('^shop/add/cart/(?P<good_id>[0-9]+)/$', views.AddCartView.as_view()),
    re_path('^shop/cart/remove/(?P<user_id>[0-9]+)/(?P<good_id>[0-9]+)/$', views.CartRemoveView.as_view()),
    re_path('^shop/add/love/(?P<good_id>[0-9]+)/$', views.AddLoveView.as_view()),
    re_path('^shop/love/remove/(?P<user_id>[0-9]+)/(?P<good_id>[0-9]+)/$', views.LoveRemoveView.as_view()),
]