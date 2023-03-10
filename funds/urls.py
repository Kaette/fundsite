from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('new-fund/', views.newFund, name='New Fund'),
        path('new-investor/', views.newInvestor, name='New Investor'),
        path('<int:fund_id>/', views.fund, name='fund'),
        path('<int:fund_id>/<int:investor_id>/', views.investor, name='fund_investor'),
        path('new-fund/succes/', views.fundSucces, name='Fund Created'),
        path('new-investor/succes/', views.investorSucces, name='Investor Created'),
]
