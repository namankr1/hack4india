from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getcategories/$', views.getcategories, name='getcategories'),
    url(r'^getsubcategories/$',views.getsubcategories, name='getsubcategories')
    ]
