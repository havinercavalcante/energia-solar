<<<<<<< HEAD
from django.db import models

class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField("Tarifa da Distribuidora", blank=True, null=True)
    discount_rule = models.ForeignKey('DiscountRule', on_delete=models.SET_NULL, null=True, blank=True)

class DiscountRule(models.Model):
    CONSUMER_TYPES = [
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
    ]
    
    consumption_range = models.CharField("Faixa de Consumo", max_length=50)
    consumer_type = models.CharField("Tipo de Consumidor", max_length=50, choices=CONSUMER_TYPES)
    cover_value = models.FloatField("Valor de Cobertura")
    discount_value = models.FloatField("Valor do Desconto")

    def __str__(self):
        return f"{self.consumer_type} - {self.consumption_range}"

=======
from django.db import models

class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField("Tarifa da Distribuidora", blank=True, null=True)
    discount_rule = models.ForeignKey('DiscountRule', on_delete=models.SET_NULL, null=True, blank=True)

class DiscountRule(models.Model):
    CONSUMER_TYPES = [
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
    ]
    
    consumption_range = models.CharField("Faixa de Consumo", max_length=50)
    consumer_type = models.CharField("Tipo de Consumidor", max_length=50, choices=CONSUMER_TYPES)
    cover_value = models.FloatField("Valor de Cobertura")
    discount_value = models.FloatField("Valor do Desconto")

    def __str__(self):
        return f"{self.consumer_type} - {self.consumption_range}"

>>>>>>> ec2fe25c217fc0007165b8fd2c342f4f5c9d1f56
