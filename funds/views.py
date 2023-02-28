from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FundForm, InvestorForm 

def index(request):
    return HttpResponse("index page")

def newFund(request):
    form = FundForm()
    if request.method == "POST":
        form = FundForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'funds/form.html', {'form': form})

def newInvestor(request):
    form = InvestorForm()
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'funds/form.html', {'form': form})

def fund(request, fund_id):
    return HttpResponse("You're at fund: %s" % fund_id)

def investor(request, investor_id):
    return HttpResponse("You're at the investor: %s" % investor_id)

def fundSucces(request):
    return HttpResponse("Fund succesfully created")

def investorSucces(request):
    return HttpResponse("Investor succesfully signed up")