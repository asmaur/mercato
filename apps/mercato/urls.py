from django.urls import include, re_path

from .views import *



urlpatterns = [
    re_path(r'^$',index),

]