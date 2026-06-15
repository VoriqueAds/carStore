from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name='Marca')
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Deletado em')
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
    def __str__(self):
        return self.name    
    
class Car(models.Model):
    model = models.CharField(max_length=100, verbose_name='Modelo')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars', verbose_name='Marca')
    factory_year = models.IntegerField(verbose_name='Ano de Fabricação')
    model_year = models.IntegerField(verbose_name='Ano do Modelo')
    color = models.CharField(max_length=50, verbose_name='Cor')
    kilometers = models.IntegerField(default=0, verbose_name='Quilometragem')
    plate = models.CharField(max_length=10, unique=True, null=True, blank=True, verbose_name='Placa')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    owner = models.CharField(max_length=100, verbose_name='Proprietário')
    description = models.TextField(verbose_name='Descrição', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name='Deletado em')
    photo = models.ImageField(upload_to='cars/', null=True, blank=True, verbose_name='Foto Principal')
    
    class Meta:
        ordering = ['model']
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    def __str__(self):
        return f'{self.brand.name} {self.model} ({self.model_year})'
    