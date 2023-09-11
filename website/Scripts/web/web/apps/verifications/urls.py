
from django.urls import path, re_path, include
from . import views

urlpatterns =[
    re_path('^ImageVerify/(?P<uuid>[\w-]+)/$', views.ImageCodeView.as_view()),
    re_path('^EmailVerify/(?P<uuid>[\w-]+)/$', views.EmailVerify.as_view()),
]