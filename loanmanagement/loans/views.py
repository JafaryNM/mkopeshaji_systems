from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class BasePage(TemplateView):
    template_name='base.html'