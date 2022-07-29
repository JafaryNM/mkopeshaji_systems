from curses.ascii import HT
from multiprocessing import context
from typing import List
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse
from django.urls import reverse_lazy
from .models import Client, Loan,LoanSchedule, Repayment
from django.views.generic import View,DetailView, TemplateView, CreateView,ListView, UpdateView,DeleteView
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



# Add loan # LoanSchedule


class CreateLoan(CreateView):
  
    template_name='loan/loan_form.html'
    template_list='loan/schedule.html'
    form_class=LoanForm
    #success_url=reverse_lazy('indexpage')


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
            #return HttpResponse(form.id)

            # Add Schedule Data
            pschedule_amount=float(amount)/float(installment)
            pinterest_amount=float(interest_amount)/float(installment)
            srepayment_date=repayment_date
            install_value=int(installment)
            
            for i in range(install_value):

            ######## CreateLoanSchedule #############
               loan_schedule = LoanSchedule.objects.create(date_schedule=srepayment_date,pamount=pschedule_amount,pinterest=pinterest_amount,loan_id=form.id)
              
        return redirect('indexpage')
    
 





               
             

          
####### Loan Schedule ##############
class SingleSchedule(DetailView):
    template_name='loan/loan_schedule.html'
    model=Loan

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schedules"] =LoanSchedule.objects.filter(loan_id=self.kwargs['pk'])
        context["loan"]=Loan.objects.filter(id=self.kwargs['pk'])
        return context
    

    


   
       

    
    
    
   
    








    


            
            


           



class DisplayScheduleLoan(ListView):
    model=LoanSchedule
    template_name='loan/loan_schedule.html'

    


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
    
    
# Workon Repayments 

class CreateRepayement(CreateView):
    model=Repayment
    fields='__all__'
    