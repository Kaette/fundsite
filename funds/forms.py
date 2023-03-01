from django.forms import ModelForm
from .models import Fund, Investor

# Forms extended from the models specified in models.py

class FundForm(ModelForm):
   class Meta:
        model = Fund
        fields = '__all__'

class InvestorForm(ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'