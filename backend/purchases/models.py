from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from Accounts.models import Accounts
from suppliers.models import Suppliers
from products.models import Product

# Create your models here.
class PurchaseStatus(models.TextChoices):
    DRAFT = 'DRAFT', ('Brouillon')
    RECEIVED = 'RECEIVED',('Reçu')
    PARTIALLY_PAID = 'PARTIALLY_PAID',('Payé partiellement')
    PAID = 'PAID',('Payé')
    CANCELLED = 'CANCELLED',('Annulé')

class Purchase(models.Model):
    purchase_number = models.CharField(('numéro achat'), max_length=50, unique=True)
    supplier = models.ForeignKey(Suppliers, on_delete=models.PROTECT, related_name='purchases')
    date_purchase = models.DateTimeField(auto_now_add=True)
    total_ht = models.DecimalField(('total HT'), max_digits=12, decimal_places=2, default=0)
    tva_rate = models.DecimalField(('taux TVA %'), max_digits=5, decimal_places=2, default=20)
    total_ttc = models.DecimalField(('total TTC'), max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=PurchaseStatus.choices, default=PurchaseStatus.DRAFT)
    paid_amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    remaining_amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True, related_name='created_purchases')
    class Meta:
        verbose_name =('Achat')
        verbose_name_plural =('Achats')
        ordering = ['-date_purchase']

    def __str__(self):
        return f"Achat #{self.purchase_number} - {self.supplier}"

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='purchase_items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='purchase_items')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
