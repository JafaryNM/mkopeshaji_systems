from django import template
from ..models import LoanSchedule,Client



register = template.Library()

@register.simple_tag
def loan_schedule():

    all_loan_schedules=LoanSchedule.objects.count()
    return all_loan_schedules







