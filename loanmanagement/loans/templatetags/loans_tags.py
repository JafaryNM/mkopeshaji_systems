from django import template
from ..models import LoanSchedule,Client



register = template.Library()

@register.simple_tag
def loan_schedule():

    all_loan_schedules=LoanSchedule.objects.count()
    return all_loan_schedules

@register.inclusion_tag('schedule.html')
def show_latest_name():
    last=Client.objects.all()
    return {'last':last}








