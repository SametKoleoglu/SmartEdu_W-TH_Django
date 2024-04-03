from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email Address'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Phone Number'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'}))

    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'email', 'phone', 'message']
