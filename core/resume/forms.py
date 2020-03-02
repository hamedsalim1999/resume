from django import forms
from .models import Article

class SendForm(forms.Form):
    tittle = forms.CharField(max_length=128,label=False ,widget=forms.TextInput(
        
        attrs={
         "autocomplete":"off",
         "class":"form-control" ,
         "placeholder":"Tittle",
    }))
    
   
    aurhor = forms.CharField(max_length=128,label=False , widget=forms.TextInput(
        
        attrs={
         "autocomplete":"off",
         "class":"form-control" ,
         "placeholder":"Aurhor",
    }))
    message = forms.CharField(label=False,widget=forms.Textarea(
        
        attrs={
         "autocomplete":"off",
         "class":"form-control" ,
         "placeholder":"Message",
    }))
    email = forms.CharField(max_length=128,label=False , widget=forms.TextInput(
        
        attrs={
         
         "autocomplete":"off",
         "class":"form-control" ,
         "placeholder":"Email",
         "type":"email",

    }))