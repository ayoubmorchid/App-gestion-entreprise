from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from products.models import Product


class StockMovement(models.Model):
    class MovementType(models.TextChoices):
        ENTRY = 'ENTRY', 'Entrée'
        EXIT = 'EXIT', 'Sortie'
        ADJUSTMENT = 'ADJUSTMENT', 'Ajustement'

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='stock_movements'
    )
    movement_type = models.CharField(
        max_length=20,
        choices=MovementType.choices
    )
    quantity = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    reference = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    comment = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='stock_movements'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Stock Movement'
        verbose_name_plural = 'Stock Movements'

    def __str__(self):
        return f"{self.product.name} - {self.get_movement_type_display()} - {self.quantity}"