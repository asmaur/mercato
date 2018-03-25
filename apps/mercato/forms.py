from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):

    class META:
        model = ContactMessage,
        fields = [
                    'full_name',
                    'company_name',
                    'email',
                    'phone',
                    'plan',
                    'subject',
                    'message' ]
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'})
        }