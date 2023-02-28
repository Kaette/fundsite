from django.forms import ModelForm
from .models import Fund, Investor

class FundForm(ModelForm):
   class Meta:
        model = Fund
        fields = '__all__'

class InvestorForm(ModelForm):
    class Meta:
        model = Investor
        exclude = ['creation_date']