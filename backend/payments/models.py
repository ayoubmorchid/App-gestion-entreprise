from django.db import models
from Accounts.models import Accounts
from sales.models import Sale
from purchases.models import Purchase
from clients.models import Client
from suppliers.models import Suppliers 

# Create your models here.
class PaymentMethod(models.TextChoices):
    CASH = 'CASH',('Espèces')
    CARD = 'CARD',('Carte')
    TRANSFER = 'TRANSFER',('Virement')
    CHECK = 'CHECK',('Chèque')

class CustomerPayment(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='customer_payments')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='customer_payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    reference = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Paiement client {self.amount} - Vente {self.sale.sale_number}"

class SupplierPayment(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='supplier_payments')
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, related_name='supplier_payments')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices)
    reference = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Paiement fournisseur {self.amount} - Achat {self.purchase.purchase_number}"


