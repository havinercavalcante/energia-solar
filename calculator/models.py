from django.db import models

class ConsumerTypes(models.TextChoices):
    RESIDENCIAL = 'Residencial'
    COMERCIAL = 'Comercial'
    INDUSTRIAL = 'Industrial'


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField("Tarifa da Distribuidora", blank=True, null=True)
    discount_rule = models.ForeignKey('DiscountRule', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class DiscountRule(models.Model):
    consumption_range = models.CharField("Faixa de Consumo", max_length=50)
    consumer_type = models.CharField("Tipo de Consumidor", max_length=50, choices=ConsumerTypes.choices)
    cover_value = models.FloatField("Valor de Cobertura")
    discount_value = models.FloatField("Valor do Desconto")

    def __str__(self):
        return f"{self.consumer_type} - {self.consumption_range}"