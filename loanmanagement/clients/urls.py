
from django.urls import path
from .views import *

urlpatterns = [
    
    
    path('Create/Customers', CreateCustomer.as_view(), name='create_customers'),
]
