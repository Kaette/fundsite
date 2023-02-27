from django import forms

class FundForm(ModelForm):
    class meta:
        model = Fund
        fields = ['name', 'description']

class InvestorForm(ModelForm):
    class meta:
        model = Investor
        fields = ['first_name', 'last_name', 'creation_date']