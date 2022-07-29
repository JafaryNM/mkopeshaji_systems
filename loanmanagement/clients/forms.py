from django import forms
from clients.models import Customer

class CustomerCreateForm(forms.ModelForm):

    class Meta:
        model=Customer
        fields='__all__'


    
