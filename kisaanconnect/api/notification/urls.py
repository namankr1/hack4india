from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pushgovtnotification/$', views.pushgovtnotification, name='pushgovtnotification'),
    url(r'^getgovtnotifications/$', views.getgovtnotifications, name='getgovtnotifications'),
    url(r'raiseinterest/$',views.raiseinterest,name='raiseinterest'),
    url(r'getnotifications/$',views.getnotifications,name = 'getnotifications'),
    url(r'negotiate/$',views.negotiate,name='negotiate'),
    url(r'endnegotiation/$',views.endnegotiation,name = 'endnegotiation')
    ]