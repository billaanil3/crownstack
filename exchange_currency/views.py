# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render
from .models import Currency

import requests
import json
import ast
# Create your views here.


def currency_details(request):
    """
    get/show currecy
    """
    all_currency = Currency.objects.all()
    return render(request, 'currency.html', {'data': all_currency})


def compare_currency(request):
    """
    compare other currencies with selected currency
    """
    base_url = "https://api.exchangeratesapi.io/latest"   # global currency API url
    compare_url = base_url + "?base=" + request.GET['currency']
    res_data = requests.get(compare_url)
    # remove unicode and converts to actual dict object from unicode object
    compared_data = ast.literal_eval(json.dumps(json.loads(res_data.text)))
    return render(request, "compared_data.html", {"data": compared_data['rates']})
