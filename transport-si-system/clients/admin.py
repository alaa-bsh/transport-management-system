
from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    # Use 'adrMAIL' instead of 'email'
    list_display = ('nom', 'prenom', 'adrMAIL', 'telephone', 'solde')
    search_fields = ('nom', 'prenom', 'adrMAIL')  # Changed here too
    
    def __str__(self):
        return f"Client {self.nom} {self.prenom}"