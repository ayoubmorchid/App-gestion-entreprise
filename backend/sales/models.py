from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from clients.models import Client

# Create your models here.

class SaleStatus(models.TextChoices):
    DRAFT = 'draft', 'Brouillon'
    CONFIRMED = 'confirmed', 'Confirmée'
    PAID = 'paid', 'Payée'
    CANCELLED = 'cancelled', 'Annulée'

class Sale(models.Model):
    sale_number = models.CharField(_('numéro vente'), max_length=50, unique=True)
    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='sales')
    date_sale = models.DateTimeField(_('date vente'), auto_now_add=True)
    total_ht = models.DecimalField(_('total HT'), max_digits=12, decimal_places=2, default=0)
    tva_rate = models.DecimalField(_('taux TVA %'), max_digits=5, decimal_places=2, default=20)
    total_ttc = models.DecimalField(_('total TTC'), max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=SaleStatus.choices, default=SaleStatus.DRAFT)
    payment_method = models.CharField(_('mode paiement'), max_length=50, blank=True)
    paid_amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    remaining_amount = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_sales')

    class Meta:
        verbose_name = _('Vente')
        verbose_name_plural = _('Ventes')
        ordering = ['-date_sale']

    def __str__(self):
        return f"{self.sale_number} - {self.client}"