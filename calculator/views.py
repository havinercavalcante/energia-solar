<<<<<<< HEAD

from django.shortcuts import render, redirect
from .forms import ConsumptionForm 
from calculator_python import calculator
import pandas as pd
from .models import Consumer, DiscountRule 
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

def calculator_view(request):
    if request.method == 'POST':
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            consumption = [
                form.cleaned_data['consumption_month1'],
                form.cleaned_data['consumption_month2'],
                form.cleaned_data['consumption_month3']
            ]
            distributor_tax = form.cleaned_data['distributor_tax']
            tax_type = form.cleaned_data['tax_type']
            result = calculator(consumption, distributor_tax, tax_type)
            context = {'result': result}
            return render(request, 'result.html', context)
    else:
        form = ConsumptionForm()
    return render(request, 'form.html', {'form': form})


def importar_xlsx(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            if file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
                
                for index, row in df.iterrows():
                    consumer, created = Consumer.objects.get_or_create(
                        document=row['Documento'],
                        defaults={
                            'name': row['Nome'],
                            'zip_code': row['Cidade'],  
                            'city': row['Cidade'],       
                            'state': row['Estado'],
                            'consumption': row['Consumo(kWh)'],
                            'distributor_tax': row['Tarifa da Distribuidora']
                        }
                    )

                    discount_rule, created = DiscountRule.objects.get_or_create(
                        consumption_range=row['Consumo(kWh)'],
                        consumer_type=row['Tipo'],              
                        defaults={
                            'cover_value': row['Cobertura(%)'],  
                            'discount_value': row['Cobertura(%)']
                        }
                    )

                    consumer.discount_rule = discount_rule
                    consumer.save()
                
                return redirect('index')  
            else:
                return render(request, 'import_error.html', {'error_message': 'O arquivo enviado não é um arquivo Excel (.xlsx).'})
        else:
            return render(request, 'import_error.html', {'error_message': 'Nenhum arquivo enviado.'})
    else:
        return render(request, 'import_form.html')

# TODO: Your list view should do the following tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1(request):
    # Create the first view here.
    pass


# TODO: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2():
    # Create the second view here.
    pass
=======

from django.shortcuts import render, redirect
from .forms import ConsumptionForm 
from calculator_python import calculator
import pandas as pd
from .models import Consumer, DiscountRule 
from django.urls import reverse


def index(request):
    return render(request, 'index.html')

def calculator_view(request):
    if request.method == 'POST':
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            consumption = [
                form.cleaned_data['consumption_month1'],
                form.cleaned_data['consumption_month2'],
                form.cleaned_data['consumption_month3']
            ]
            distributor_tax = form.cleaned_data['distributor_tax']
            tax_type = form.cleaned_data['tax_type']
            result = calculator(consumption, distributor_tax, tax_type)
            context = {'result': result}
            return render(request, 'calculator/result.html', context)
    else:
        form = ConsumptionForm()
    return render(request, 'calculator/form.html', {'form': form})


def importar_xlsx(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            if file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
                
                for index, row in df.iterrows():
                    consumer, created = Consumer.objects.get_or_create(
                        document=row['Documento'],
                        defaults={
                            'name': row['Nome'],
                            'zip_code': row['Cidade'],  
                            'city': row['Cidade'],       
                            'state': row['Estado'],
                            'consumption': row['Consumo(kWh)'],
                            'distributor_tax': row['Tarifa da Distribuidora']
                        }
                    )

                    discount_rule, created = DiscountRule.objects.get_or_create(
                        consumption_range=row['Consumo(kWh)'],
                        consumer_type=row['Tipo'],              
                        defaults={
                            'cover_value': row['Cobertura(%)'],  
                            'discount_value': row['Cobertura(%)']
                        }
                    )

                    consumer.discount_rule = discount_rule
                    consumer.save()
                
                return redirect('index')  
            else:
                return render(request, 'import_error.html', {'error_message': 'O arquivo enviado não é um arquivo Excel (.xlsx).'})
        else:
            return render(request, 'import_error.html', {'error_message': 'Nenhum arquivo enviado.'})
    else:
        return render(request, 'import_form.html')

# TODO: Your list view should do the following tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1(request):
    # Create the first view here.
    pass


# TODO: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2():
    # Create the second view here.
    pass
>>>>>>> ec2fe25c217fc0007165b8fd2c342f4f5c9d1f56
