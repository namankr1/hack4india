from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pushgovtnotification/$', views.pushgovtnotification, name='pushgovtnotification'),
    url(r'^getgovtnotifications/$', views.getgovtnotifications, name='getgovtnotifications'),
    url(r'raiseinterest/$',views.raiseinterest,name='raiseinterest'),
    url(r'getnotifications/$',views.getnotifications,name = 'getnotifications'),
    url(r'negotiate/$',views.negotiate,name='negotiate'),
    url(r'endnegotiation/$',views.endnegotiation,name = 'endnegotiation'),
    url(r'getnegotiationsofuser/$',views.getnegotiationsofuser,name = 'getnegotiationsofuser'),
    url(r'getordersofuser/$',views.getordersofuser,name = 'getordersofuser'),
    url(r'getmarketinsights/$',views.getmarketinsights,name = 'getmarketinsights')
    ]