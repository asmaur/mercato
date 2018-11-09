from django.urls import include, re_path, path

from .views import *



urlpatterns = [
    re_path(r'^$',index),
    re_path(r'^business-divisions$',business),
    re_path(r'^services$',services),
    re_path(r'^about$',about),
    re_path(r'^contact$',contact),
    re_path(r'^sendmail/$',contact_message),
    re_path(r'^paper-pulp$',paper_pulp),
    re_path(r'^footwear-acessorie$',calcados),
    re_path(r'^steel-aluminium$',steel),
    re_path(r'^agri-business$',agri_business),
    re_path(r'^terms-conditions$',terms),
    re_path(r'^news/$',news_letters),

]