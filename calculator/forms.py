from django import forms

class ConsumptionForm(forms.Form):
    consumption_month1 = forms.FloatField(label='Consumo do Mês 1')
    consumption_month2 = forms.FloatField(label='Consumo do Mês 2')
    consumption_month3 = forms.FloatField(label='Consumo do Mês 3')
    distributor_tax = forms.FloatField(label='Distributor Tax')
    tax_type = forms.ChoiceField(choices=[('Residencial', 'Residencial'), ('Comercial', 'Comercial'), ('Industrial', 'Industrial')])
