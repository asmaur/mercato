from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import (AddressNotFoundError, AuthenticationError, GeoIP2Error, HTTPError,
                           InvalidRequestError, OutOfQueriesError, PermissionRequiredError)
from django.template import RequestContext, Context
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
import json

from .models import *
from pprint import pprint

#from django.utils.translation import gettext as _
# Create your views here.



def get_ip(request):

    try:
        x_forward = request.META.get("HTTP_X_FORWARD_FOR")
        ip_remote = request.META.get("REMOTE_ADDR")

        if ip_remote:
            #print("IP: ", request.META.get("REMOTE_ADDR"))
            ip = ip_remote
        else:
            x_forward = request.META.get("HTTP_X_FORWARD_FOR")
            #print("x_forward: ", x_forward)
            ip = x_forward

    except:
        ip = None
        print("Empty IP field")

    return ip


def user_data(request, ip):
    g = GeoIP2(settings.GEOIP_PATH)

    try:
        g.city(ip)
        data = g.city(ip)#'191.32.38.236')
        print(data)
        city = data["city"]
        country_code = data["country_code"]
        country_name = data["country_name"]
        dma_code = data["dma_code"]
        latitude = data["latitude"]
        longitude = data["longitude"]
        postal_code = data["postal_code"]
        region = data["region"]

        userdata = VisiterData(ip = ip, city = data["city"], country_code = data["country_code"], country_name = data["country_name"], 
            dma_code = data["dma_code"], latitude = data["latitude"], longitude = data["longitude"], postal_code = data["postal_code"], region = data["region"])

        userdata.save()

        print("User data saved")

    except Exception:
        data =""

    return 



def index(request):
    ip = get_ip(request)
    print(user_data(request, ip))
    return render(request, "mercato/index.html",)


def news_letters(request):
    resp = None

    if request.method == "POST":
        data = json.loads(  request.body.decode('utf-8'))
        
        try:
            print("trying")
            news = NewsLetters(full_name = data["full_name"], email = data["email"], fone_number = data["fone_number"] )
            news.save()
            resp = {"sent": True}

        except Exception as ex:            
            print(ex)
            resp = {"sent": False}

    print(resp)
    return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))


def contact_message(request):

    message = None  # "Erro ao enviar a mensagem ..!"
    resp = 'resposta sent'
    

    if request.method == "POST":
        
        data = json.loads(request.body.decode('utf-8'))
        
        #full_name = request.POST["full_name"]
        #company_name = request.POST["company_name"]
        #email = post["email"]
        #phone = post["phone"]
        #plan = post["plan"]
        #subject = post["subject"]
        #message = post["message"]

        try:
            contact = ContactMessage(full_name = data["full_name"], company_name =  data["company_name"], email =  data["email"], phone =  data["phone"],
             plan =  data["plan"], subject =  data["subject"], message = data["message"] )
            contact.save()
            resp = {"sent": True}

        except Exception as ex:
            
            print(ex)
            resp = {"sent": False}
    

    return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))

