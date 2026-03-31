from django.db import models
from Accounts.models import Accounts

class Category(models.Model):
    name = models.CharField(('nom'), max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('Catégorie')
        verbose_name_plural = ('Catégories')
        ordering = ['name']

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(('nom'), max_length=255)
    description = models.TextField(blank=True)

    category = models.ForeignKey(
        Category,  
        on_delete=models.SET_NULL,
        null=True,
        related_name='products'
    )

    reference = models.CharField(('référence'), max_length=100, unique=True)
    barcode = models.CharField(('code-barres'), max_length=50, blank=True)
    purchase_price = models.DecimalField(('prix achat'), max_digits=10, decimal_places=2, default=0)
    sale_price = models.DecimalField(('prix vente'), max_digits=10, decimal_places=2)
    stock_quantity = models.DecimalField(('quantité stock'), max_digits=10, decimal_places=2, default=0)
    alert_threshold = models.DecimalField(('seuil alerte'), max_digits=10, decimal_places=2, default=5)
    unit = models.CharField(('unité'), max_length=20, default='unit')
    image = models.ImageField(('image'), upload_to='products/', blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        Accounts,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_products'
    )

    class Meta:
        verbose_name = ('Produit')
        verbose_name_plural = ('Produits')
        ordering = ['name']

    def __str__(self):
        return self.name