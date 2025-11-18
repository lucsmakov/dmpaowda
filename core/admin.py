from django.contrib import admin
from core.models import Cliente, Veiculo, Fabricante

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Fabricante)
admin.site.register(Veiculo)