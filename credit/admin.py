from django.contrib import admin
from credit.models import LoanRequest


class LoanRequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(LoanRequest, LoanRequestAdmin)
