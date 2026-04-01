from django.db import models

TYPE_CHOICES = [
    ('entreprise', 'Entreprise'),
    ('associe', 'Associé'),
    ('particulier', 'Particulier'),
]

# Create your models here.
class Suppliers (models.Model):
    nom = models.CharField(max_length=200)
    type_suppliers = models.CharField(max_length=20, choices=TYPE_CHOICES, default='particulier')
    ice = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.TextField()
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100, default='Maroc')
    contact_principal = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)