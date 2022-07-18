from typing import List
from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from .models import Client, Loan,LoanSchedule
from django.views.generic import View, TemplateView, CreateView,ListView, UpdateView,DeleteView
from .forms import LoanForm
from itertools import repeat
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



# Add loan


class CreateLoan(CreateView):
  
    template_name='loan/loan_form.html'
    template_list='loan/loans.html'
    form_class=LoanForm
    success_url=reverse_lazy('indexpage')


    # Add Loan
    def  post(self, request, *args, **kwargs):
        form=LoanForm(request.POST)
        if form.is_valid:
            form=form.save(commit=False)
            form.created_by=request.user
            form.save()
            # Get Value  From form
            amount=form.amount
            repayement_date = form.repayment_date
            interest_amount = form.interest_amount
            interest_amount = form.interest_amount
            installment = form.installment
            repayment_date= form.repayment_date

            # Add Schedule Data
            pschedule_amount=float(amount)/float(installment)
            pinterest_amount=float(interest_amount)/float(installment)
            srepayment_date=repayment_date
            # Insert Data to
            loan_schedule = LoanSchedule.objects.create(date_schedule=srepayment_date,pamount=pschedule_amount,pinterest=pinterest_amount,loan_id=form.id)

            # Take data to database

            pschedule_values=[]

            pschedule_values.extend(repeat(pschedule_amount,installment))
            for pschedule_value in pschedule_values:

                return HttpResponse(pschedule_value)











class AddSchedule(View):
    
    template_name='loan/schedule.html'
    model=LoanSchedule
    
    def get(request,*args,**kwargs):
        return render(self.template_name)
        
    
# Display  Loan

class DisplayLoan(ListView):
    model=Loan
    template_name='loan/loans.html'
    
    def get_context_data(self, **kwargs):
        context = super(DisplayLoan, self).get_context_data(**kwargs)
        context['loans']=Loan.objects.all()
        return context

# Update Loan
class UpdateLoan(UpdateView):
    model=Loan
    template_name='loan/update_loan.html'
    fields='__all__'
    success_url=reverse_lazy('display_loans')

# Delete Loan

class DeleteLoan(DeleteView):
    model=Loan
    template_name='loan/delete.html'
    success_url=reverse_lazy('indexpage')
    
    
# Display Schedule

        
        
    
    
      
      
    
    
    
    
    
    



















    
        
            
            
            
             
       






















    
