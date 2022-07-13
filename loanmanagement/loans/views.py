from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Client
from django.views.generic import TemplateView, CreateView,ListView, UpdateView,DeleteView

# Create your views here.


class BasePage(TemplateView):
    template_name='base.html'


# Add New Customers

class ClientCreate(CreateView):
    
    model=Client
    template_name='clients/client_form.html'
    fields='__all__'
    success_url= reverse_lazy('indexpage')
    
# Display Customers

class DisplayClient(ListView):
    model=Client
    template_name='clients/clients.html'
    
    
    def get_context_data(self, **kwargs):
        context = super(DisplayClient, self).get_context_data(**kwargs)
        context['clients']=Client.objects.all()
        return context
    

# Update Clients

class UpdateClient(UpdateView):
    model=Client
    templete_name='clients/update_client.html'
    fields='__all__'
    success_url=reverse_lazy('indexpage')


# Delete Client

class DeleteClient(DeleteView):
    model=Client
    template_name='clients/delete.html'
    success_url=reverse_lazy('indexpage')
    
    
    
    
    
    
