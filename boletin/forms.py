from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model=Registrado
        fields = ["nombre","email"]
        
    def clean_email(self):
        email=self.cleaned_data.get("email")
        return email
    def clean_nombre(self):
        nombre=self.cleaned_data.get("nombre")
        return nombre


class ContactForm(forms.Form):
    nombre= forms.CharField()
    email=forms.EmailField()
    mensaje= forms.CharField(widget=forms.Textarea)
    
##    def clean_email(self):
##        email=self.cleaned_data.get("email")
##        return email