<<<<<<< HEAD
import pandas as pd
from calculator.models import Consumer, DiscountRule 

# Ler o arquivo Excel
df = pd.read_excel('projeto/haviner/consumers.xlsx')

existing_discount_rules = {}

for index, row in df.iterrows():
    discount_rule_key = (row['Tipo de Consumidor'], row['Faixa de Consumo'])
    if discount_rule_key in existing_discount_rules:
        discount_rule = existing_discount_rules[discount_rule_key]
    else:
        discount_rule = DiscountRule.objects.create(
            consumption_range=row['Faixa de Consumo'],
            consumer_type=row['Tipo de Consumidor'],
            cover_value=row['Valor de Cobertura'],
            discount_value=row['Valor do Desconto']
        )
        existing_discount_rules[discount_rule_key] = discount_rule

    consumer = Consumer.objects.create(
        name=row['Nome'],
        document=row['Documento(CPF/CNPJ)'],
        zip_code=row['CEP'],
        city=row['Cidade'],
        state=row['Estado'],
        consumption=row['Consumo(kWh)'],
        distributor_tax=row['Tarifa da Distribuidora'],
        discount_rule=discount_rule
    )
=======
import pandas as pd
from calculator.models import Consumer, DiscountRule 

# Ler o arquivo Excel
df = pd.read_excel('projeto/haviner/consumers.xlsx')

existing_discount_rules = {}

for index, row in df.iterrows():
    discount_rule_key = (row['Tipo de Consumidor'], row['Faixa de Consumo'])
    if discount_rule_key in existing_discount_rules:
        discount_rule = existing_discount_rules[discount_rule_key]
    else:
        discount_rule = DiscountRule.objects.create(
            consumption_range=row['Faixa de Consumo'],
            consumer_type=row['Tipo de Consumidor'],
            cover_value=row['Valor de Cobertura'],
            discount_value=row['Valor do Desconto']
        )
        existing_discount_rules[discount_rule_key] = discount_rule

    consumer = Consumer.objects.create(
        name=row['Nome'],
        document=row['Documento(CPF/CNPJ)'],
        zip_code=row['CEP'],
        city=row['Cidade'],
        state=row['Estado'],
        consumption=row['Consumo(kWh)'],
        distributor_tax=row['Tarifa da Distribuidora'],
        discount_rule=discount_rule
    )
>>>>>>> ec2fe25c217fc0007165b8fd2c342f4f5c9d1f56
