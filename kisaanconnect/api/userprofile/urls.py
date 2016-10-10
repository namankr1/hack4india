from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signin/$',views.signin, name='signin'),
    url(r'^verifyotp/$', views.verifyOTP, name='verifyotp'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^sendotp/$', views.sendOTP, name='sendotp'),
    url(r'^getprofile/$',views.getprofile,name='getprofile'),
    url(r'^changepassword/$', views.changepassword, name='changepassword'),
    url(r'^forgotpassword/$', views.forgotpassword, name='forgotpassword'),
    url(r'^profileupdate/$', views.profileupdate, name='profileupdate')
    ] 
