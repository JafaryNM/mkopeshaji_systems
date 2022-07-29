from django.contrib import admin
from .models import LoanSchedule, Loan,Client


admin.site.register(LoanSchedule)
admin.site.register(Client)
admin.site.register(Loan)





