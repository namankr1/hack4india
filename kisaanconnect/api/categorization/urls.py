from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^getcategories/$', views.getcategories, name='getcategories'),
    url(r'^getsubcategories/$',views.getsubcategories, name='getsubcategories'),
    url(r'^addsubcategories/$',views.addsubcategories, name='addsubcategories'),
    url(r'^addcategories/$', views.addcategories, name='addcategories')
    ]
