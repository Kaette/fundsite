from django.contrib import admin

# Register your models here.

from .models import Investor
admin.site.register(Investor)

from .models import Fund
admin.site.register(Fund)