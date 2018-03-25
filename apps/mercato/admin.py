from django.contrib import admin
from .models import *
# Register your models here.

class NewsLettersAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'fone_number', 'email')


class VisiterDataAdmin(admin.ModelAdmin):
	
	list_display = ('ip','country_name', 'city','region', 'visits')

class ContactAdmin(admin.ModelAdmin):
	
	list_display = ( 'subject','full_name','company_name', 'email','phone', 'plan')
	


admin.site.register(NewsLetters, NewsLettersAdmin)
admin.site.register(VisiterData, VisiterDataAdmin)
admin.site.register(ContactMessage,ContactAdmin)