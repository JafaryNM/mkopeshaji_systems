
from django.urls import path
from .views import BasePage,ClientCreate,DisplayClient,UpdateClient,DeleteClient,CreateLoan,DisplayLoan,UpdateLoan,DeleteLoan



urlpatterns = [
    
    
    ################### CLIENTS URLS #############################
    
    path('', BasePage.as_view(), name='indexpage'),
    path('Clients/Create/', ClientCreate.as_view(), name='create_client'),
    path('Clients/', DisplayClient.as_view(), name='display_clients'),
    path('Clients/<int:pk>/Update/', UpdateClient.as_view(), name='update_clients'),
    path('Clents/<int:pk>/Delete',DeleteClient.as_view(), name='delete_client' ),
 
  #################### LOAN URLS ##############################
   
   path('Loan/Create/',CreateLoan.as_view(), name='create_loan' ),
   path('Loans/',DisplayLoan.as_view(), name='display_loans'),
   path('Loans/<int:pk>/Update',UpdateLoan.as_view(), name='update_loan' ),
   path('Loan/<int:pk>/Delete/', DeleteLoan.as_view(), name='delete_loan'),
   
   
   ################## SCHEDULE URL ###########################
   #path('LoanSchedule/',DisplaySchedule.as_view(), name='display_schedule')
    
]