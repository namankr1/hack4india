from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^addquote/$', views.addquote, name='addquote'),
    url(r'^getquote/$', views.getquote, name='getquote'),
    url(r'^getquotebyuser/$', views.getquotebyuser, name='getquotebyuser'),
    url(r'^getallquotesbyuser/$', views.getallquotesbyuser, name='getallquotesbyuser'),
    url(r'^deletequote/$', views.deletequote, name='deletequote'),
    url(r'^updatequote/$', views.updatequote, name='updatequote'),
    url(r'^searchquotes/$',views.searchquotes, name='searchquotes')
    ]
