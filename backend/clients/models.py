
TYPE_CHOICES = [
    ('entreprise', 'Entreprise'),
    ('associe', 'Associé'),
    ('particulier', 'Particulier'),
]

class Client(models.Model):
    nom = models.CharField(max_length=200)
    type_client = models.CharField(max_length=20, choices=TYPE_CHOICES, default='particulier')
    raison_sociale = models.CharField(max_length=200, blank=True)
    ice = models.CharField(max_length=20, blank=True)
    ifu = models.CharField(max_length=20, blank=True)
    rc = models.CharField(max_length=20, blank=True)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.TextField()
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100, default='Maroc')
    contact_principal = models.CharField(max_length=200, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.nom
