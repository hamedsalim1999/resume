from django.forms import ModelForm,Textarea,TextInput,EmailInput
from .models import Form


class SendForm(ModelForm):
    class Meta:
        model = Form
        fields  = ( 'tittle' , 'message','auther','email')
        




        labels = {
        "tittle": False,
        "message": False,
        "auther": False,
        "email": False,
    }
        widgets = {
            'message': Textarea(
                attrs={ 
        "autocomplete":"off",
        "class":"form-control" ,
        "placeholder":"Message"},

        
        ),
        'tittle': TextInput( 
            attrs={ 
        "autocomplete":"off",
        "class":"form-control" ,
        "placeholder":"tittle"},
        
        ),
        'auther': TextInput( 
            attrs={ 
        "autocomplete":"off",
        "class":"form-control" ,
        "placeholder":"auther"},
        
        ),
        'email': EmailInput( 
            attrs={ 
        "autocomplete":"off",
        "class":"form-control" ,
        "placeholder":"email"},
        
        ),
        
        }
       