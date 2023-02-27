from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("index page")

def newFund(request):
    form = FundForm()
    return HttpResponse(form)

def newInvestor(request):
    return HttpResponse("You're at the funds index")

def fund(request, fund_id):
    return HttpResponse("You're at fund: %s" % fund_id)

def investor(request, investor_id):
    return HttpResponse("You're at the investor: %s" % investor_id)