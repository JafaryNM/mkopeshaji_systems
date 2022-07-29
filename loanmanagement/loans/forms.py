from django import forms
from .models import Loan,Repayment
from .widget import DatePickerInput

class LoanForm(forms.ModelForm):
    
    class Meta:
        model = Loan
        fields = '__all__'
        widgets = {
            'loan_date' : DatePickerInput(),
             'repayment_date': DatePickerInput()
           }

class RepaymentsForm(forms.ModelForm):

    class Meta:
        model= Repayment
        fields='__all__'
