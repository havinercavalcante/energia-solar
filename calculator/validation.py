from .models import Consumer
from django import forms

def validate_cpf(cpf):
    cpf = ''.join(c for c in cpf if c.isdigit())

    if len(cpf) != 11 or cpf == '00000000000' or cpf == '11111111111' or cpf == '22222222222' or cpf == '33333333333' or cpf == '44444444444' or cpf == '55555555555' or cpf == '66666666666' or cpf == '77777777777' or cpf == '88888888888' or cpf == '99999999999':
        return False

    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0

    if resto != int(cpf[9]):
        return False

    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        resto = 0

    if resto != int(cpf[10]):
        return False

    return True

def validate_cnpj(cnpj):
    cnpj = ''.join(c for c in cnpj if c.isdigit())

    if len(cnpj) != 14:
        return False

    if cnpj == '00000000000000' or cnpj == '11111111111111' or cnpj == '22222222222222' or cnpj == '33333333333333' or cnpj == '44444444444444' or cnpj == '55555555555555' or cnpj == '66666666666666' or cnpj == '77777777777777' or cnpj == '88888888888888' or cnpj == '99999999999999':
        return False

    soma = 0
    peso = 2
    for i in range(11, -1, -1):
        soma += int(cnpj[i]) * peso
        peso += 1
        if peso == 10:
            peso = 2

    resto = soma % 11
    if resto < 2:
        digito_verificador_1 = 0
    else:
        digito_verificador_1 = 11 - resto

    if int(cnpj[12]) != digito_verificador_1:
        return False

    soma = 0
    peso = 2
    for i in range(12, -1, -1):
        soma += int(cnpj[i]) * peso
        peso += 1
        if peso == 10:
            peso = 2

    resto = soma % 11
    if resto < 2:
        digito_verificador_2 = 0
    else:
        digito_verificador_2 = 11 - resto

    if int(cnpj[13]) != digito_verificador_2:
        return False

    return True

def clean(document):
    if Consumer.objects.filter(document=document).exists():
        raise forms.ValidationError('Este documento já está cadastrado.')

    return document
