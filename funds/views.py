from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FundForm, InvestorForm
from .models import Fund, Investor

def index(request):
    funds = Fund.objects.order_by('-name')
    return render(request, 'funds/index.html', {'funds': funds})

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
    # Show name
    # List investors
    # members = Investor.objects.filter(fund=fund_id)
    # return render(request, 'funds/fund.html', {'members': members})
    return 0

def investor(request, investor_id):
    #investor = get_object_or_404(first_name, pk=investor_id)
    #return render(request, 'funds/investor.html', {})
    return 0

def fundSucces(request):
    return HttpResponse("Fund succesfully created")

def investorSucces(request):
    return HttpResponse("Investor succesfully signed up")