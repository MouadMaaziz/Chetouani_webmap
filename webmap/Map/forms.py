from django import forms

class ContactForm(forms.Form):
    Email= forms.EmailField(required=True)
    Name= forms.CharField(required=True)
    message= forms.CharField(widget=forms.Textarea,required=True)
