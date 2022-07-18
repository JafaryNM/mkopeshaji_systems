from django.contrib import admin
from .models import LoanSchedule, Loan,Client


#admin.site.register(LoanSchedule)
#admin.site.register(Client)
#admin.site.register(Loan)

# Register your models here.
@admin.register(LoanSchedule)
class ScheduleAdmin(admin.ModelAdmin):

    list_display=('pamount','date_schedule','pinterest','loan')



