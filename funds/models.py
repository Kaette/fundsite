from django.db import models

# Specifies two models Fund and Investor which make the data used in the app.
# Extends to forms in forms.py

class Fund(models.Model):
    fund = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.fund

class Investor(models.Model):
    investor = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)

    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.investor, self.last_name)
    
    class Meta:
        ordering = ['last_name']