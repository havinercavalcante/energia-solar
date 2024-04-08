from django import forms
from .models import Consumer, ConsumerTypes
from .validation import validate_cpf, validate_cnpj


class ConsumptionForm(forms.Form):
    consumption_month1 = forms.FloatField(label='Consumo do Mês 1')
    consumption_month2 = forms.FloatField(label='Consumo do Mês 2')
    consumption_month3 = forms.FloatField(label='Consumo do Mês 3')
    distributor_tax = forms.FloatField(label='Distributor Tax')
    tax_type = forms.ChoiceField(label="Tipo de Consumidor", choices=ConsumerTypes.choices)


class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['name', 'document', 'zip_code', 'city', 'state', 'consumption', 'distributor_tax',]

    def clean_document(self):
        document_type = self.cleaned_data.get('document_type')
        document = self.cleaned_data.get('document')

        if document_type == 'CPF':
            if not validate_cpf(document):
                raise forms.ValidationError('CPF inválido ou já cadastrado.')
        elif document_type == 'CNPJ':
            if not validate_cnpj(document):
                raise forms.ValidationError('CNPJ inválido ou já cadastrado.')

        return document

    def clean(self):
        cleaned_data = super().clean()
        document = cleaned_data.get('document')

        if Consumer.objects.filter(document=document).exists():
            raise forms.ValidationError('Este documento já está cadastrado.')

        return cleaned_data