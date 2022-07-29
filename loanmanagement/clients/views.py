from django.shortcuts import render
from django.views.generic import CreateView
from clients.models import Customer
from clients.forms import CustomerCreateForm


class CreateCustomer(CreateView):
   model=Customer
   template_name='clients/customers_form.html'
   form_class= CustomerCreateForm
   

  
   def get(self,request,*args,**kwargs):
    return render(request,self.template_name,{'form':self.form_class})
   

    