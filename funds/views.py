from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .forms import FundForm, InvestorForm
from .models import Fund, Investor

# The main page where the user can continue to signup or lookup data.
def index(request):
    # Lists registered funds and orders them by the primary key.
    funds = Fund.objects.order_by('-id')
    return render(request, 'funds/index.html', {'funds': funds})

# Generates the form for added new funds to the database.
def newFund(request):
    # FundForm() specified in forms.py.
    form = FundForm()
    # Validates the request as POST and adds to database.
    if request.method == "POST":
        form = FundForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'funds/form.html', {'form': form})

# Generates Investor signup form same as above.
def newInvestor(request):
    form = InvestorForm()
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'funds/form.html', {'form': form})

# Fetches the fund which primary key matches the number in the url.
def fund(request, fund_id):
    name = get_object_or_404(Fund, pk=fund_id)
    # Lists investors belonging to the given fund.
    members = Investor.objects.filter(fund=name)
    return render(request, 'funds/fund.html', {'members': members, 'name': name})

# Generates page for investor same as fund. Takes both investor_id and fund_id as it is a subsite.
def investor(request, investor_id, fund_id):
    # Show name
    investor = get_object_or_404(Investor, pk=investor_id)
    fund = get_object_or_404(Fund, pk=fund_id)
    return render(request, 'funds/investor.html', {'investor': investor, 'fund': fund})

def fundSucces(request):
    return HttpResponse("Fund succesfully created")

def investorSucces(request):
    return HttpResponse("Investor succesfully signed up")