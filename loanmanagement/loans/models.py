

from django.db import models
from datetime import datetime , date

# Create your models here.
GENDER_CHOICES = (
    
    ("Male", "Male"),
    ("Female", "Female"),
    
)

################### CLIENT MODEL ###################
class Client(models.Model):
    
    name = models.CharField(max_length = 150, null=True,)
    mobile= models.IntegerField(max_length=20, null=True)
    location = models.CharField(max_length = 150)
    gender = models.CharField(max_length = 40, choices=GENDER_CHOICES, default='Male')
    
    def __str__(self):
        
        return self.name
    

################### LOAN MODEL #####################
    
class Loan(models.Model):
    amount=models.FloatField(max_length=300, null=True)
    installment = models.IntegerField(null=True)
    interest_amount=models.FloatField(max_length=300 ,null=True)
    loan_date = models.DateField(auto_now=False , null=True , blank=True )
    repayment_date = models.DateField(auto_now=False , null=True , blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
   
    
    def __str__(self):
        
        return self.amount
    
    

############### LOAN SCHEDULE ######################
class  LoanSchedule(models.Model):
    date_schedule = models.DateField(auto_now=False, auto_now_add=False ,null= True, blank=True)
    pamount = models.FloatField()
    pinterest = models.FloatField()
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)

    def __str__(self):
        return self.pamount
    

###################### REPAYMENT MODEL #################

class Repayment(models.Model):
    
  payment_date = models.DateField(auto_now=True)
  amount = models.FloatField(null=True)
  principlepaid = models.FloatField(null=True)
  interest_paid = models.FloatField(null=True)
  loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
  loan_schedule = models.ForeignKey(LoanSchedule, on_delete=models.CASCADE)
  
  def __str__(self):
      
      return self.payment_date
  
  
  
  
  
  
  


    
    
    
    
    
    
     
     
     

     
     
     
     
     
     
     
    