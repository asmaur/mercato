from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.template import RequestContext, Context
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError, EmailMessage
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
    #ip = get_ip(request)
    #print(user_data(request, ip))
    return render(request, "mercato/index.html",)

def business(request):
    return render(request, "mercato/busi.html")

def services(request):
    return render(request, "mercato/services.html")

def about(request):
    return render(request, "mercato/about.html")

def contact(request):
    return render(request, "mercato/contact.html")

def paper_pulp(request):
    return render(request, "mercato/papel.html")

def agri_business(request):
    return render(request, "mercato/aggro.html")

def steel(request):
    return render(request, "mercato/steel.html")

def calcados(request):
    return render(request, "mercato/calca.html")

def terms(request):
    return render(request, "mercato/terms-conditions.html")

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
    data = json.loads(request.body.decode("utf-8"))
    print(data['full_name'])

    if request.method == "POST":
        name = data['full_name']
        company = data['company_name']
        mail = data['email']
        phone = data['phone']
        subject = data['subject']
        mes = data['message']

        message = 'Company: '+ company+'\n'+ 'Subjet: '+ subject +'\n'+ 'Phone: '+ phone + '\n'+ 'Email: '+ mail+ '\n'+ 'message: '+ mes
        print(message)
        #reply_to = [mail],from_email=mail,headers={'Content-Type': 'text/plain'},
        try:
            ctx = {
                'name':name,
                'company':company,
                'subject':subject,
                'phone':phone,
                'message':mes
            }
            mailing = render_to_string('mercato/sentmail.htm', ctx)
            email = EmailMessage(
                subject,
                mailing,
                from_email='contact@br-mercato.com',
                to=['contact@br-mercato.com'],
                reply_to=[mail],

            )
            email.content_subtype = 'html'
            email.send()


            #send_mail(subject, message, mail, ['contact@br-mercato.com'])
            resp = {"sent": True}

        except Exception as ex:
            
            print(ex)
            resp = {"sent": False}
    

    return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))

def error_404_view(request, exception):
    return render(request,'mercato/error.html', {}, status=404)

def error_403_view(request, exception):
    return render(request,'mercato/error.html', {}, status=403)