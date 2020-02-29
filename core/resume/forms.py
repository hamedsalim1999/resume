from django import forms
from .models import Article

class SendForm(forms.Form):
    tittle = forms.CharField(max_length=128)
    slug = forms.SlugField()
    message = forms.CharField(widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Article.category_list.objects)
    aurhor = forms.CharField(max_length=128)
    email = forms.EmailField()