from django.urls import path, re_path
from . import views


urlpatterns =[
    re_path('^register/$', views.RegisterView.as_view(),name='register'),
    re_path('^username/(?P<username>[-a-zA-Z0-9]{4,32})/count/$',views.UserNameCheckView.as_view(), name='CheckUsername'),
    re_path('^Logout/$', views.LogoutView.as_view(), name='Logout'),
    re_path('^phone/(?P<phone>[2-9][0-9]{2}[2-9][0-9]{2}[0-9]{4})/count/$', views.PhoneCheckView.as_view()),
    re_path('^Login/$', views.LoginView.as_view(), name='Login'),

]