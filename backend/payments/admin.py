from django.contrib import admin

from backend.payments.models import CustomerPayment,SupplierPayment

# Register your models here.
admin.site.register(SupplierPayment)
admin.site.register(CustomerPayment)

