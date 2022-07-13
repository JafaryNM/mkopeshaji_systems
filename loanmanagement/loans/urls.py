
from django.urls import path
from .views import BasePage,ClientCreate,DisplayClient,UpdateClient,DeleteClient



urlpatterns = [
    
    path('', BasePage.as_view(), name='indexpage'),
    path('Clients/Create/', ClientCreate.as_view(), name='create_client'),
    path('Clients/', DisplayClient.as_view(), name='display_clients'),
    path('Clients/<int:pk>/Update/', UpdateClient.as_view(), name='update_clients'),
    path('Clents/<int:pk>/Delete',DeleteClient.as_view(), name='delete_client' )
 
    
]