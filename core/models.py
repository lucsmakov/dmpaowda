from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    endereço = models.CharField(max_length=150, verbose_name='Endreço', blank=True, null=True)
    complemento = models.CharField(max_length=50, verbose_name='Complemento', blank=True, null=True)
    bairro = models.CharField(max_length=50, verbose_name='Bairro', blank=True, null=True)
    cidade = models.CharField(max_length=100, verbose_name='Cidade', blank=True, null=True)
    cep = models.CharField(max_length=10, verbose_name='Cep', blank=True, null=True)
    telefone = models.CharField(max_length=15, verbose_name='Fone', blank=True, null=True)
    email = models.EmailField(verbose_name='email')
    foto = models.ImageField(upload_to='image_Clients', verbose_name='foto', blank=True, null=True)
  
    def __str__(self):
        return self.nome
    
    
class Fabricante(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False, verbose_name='Marca')
    logo = models.ImageField(upload_to='image_fabricante', verbose_name='Marca', blank=True, null=False)
    site = models.CharField(max_length=200, verbose_name='site')
    
    def __str__(self):
        return self.nome
    

class Veiculo(models.Model):
        id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
        id_fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE)
        modelo = models.CharField(max_length=100, blank=True, null=False, verbose_name='modelo')
        ano = models.IntegerField(default=2025, blank=False, null=False, verbose_name='Ano')
        cor = models.CharField(max_length=100, blank=False, null=False, verbose_name='Cor')
        placa = models.CharField(max_length=8, blank=False, null=False, verbose_name='Placa')
        foto = models.ImageField(upload_to='image_veiculo', blank=True, null=True, verbose_name='foto')
        
        def __str__(self):
             return f"{self.modelo} - {self.placa}"
        
        