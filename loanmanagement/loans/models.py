
from django.db import models


# Create your models here.
GENDER_CHOICES = (
    
    ("Male", "Male"),
    ("Female", "Female"),
    
)

################### CLIENT MODEL ###################
class Client(models.Model):
    
    first_name = models.CharField(max_length = 150, null=True)
    address = models.CharField(max_length = 150, null=True)
    location = models.CharField(max_length = 150)
    gender = models.CharField(max_length = 40, choices=GENDER_CHOICES, default='Male')
    
    def __str__(self):
        
        return self.first_name
    

################### LOAN MODEL #####################
    
class Loan(models.Model):
    amount=models.FloatField(max_length=50, null=True)
    installment = models.IntegerField(null=True)
    loan_date = models.DateField(auto_now=True)
    repayment_date = models.DateField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fieldName = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        
        return self.amount
    
    

############### LOAN SCHEDULE ######################
class  LoanSchedule(models.Model):
    date_schedule = models.DateField(auto_now=False, auto_now_add=False)
    amount = models.FloatField()
    interest = models.FloatField()
    principle= models.FloatField()
    status = models.CharField(max_length=20)
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    

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
  
  
  
  
  
  
  


    
    
    
    
    
    
     
     
     

     
     
     
     
     
     
     
    