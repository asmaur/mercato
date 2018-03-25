from django.urls import include, re_path, path

from .views import *



urlpatterns = [
    re_path(r'^$',index),
    re_path(r'^contact/$',contact_message),
    re_path(r'^news/$',news_letters),

]