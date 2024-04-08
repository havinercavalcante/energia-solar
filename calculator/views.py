
from django.shortcuts import render, redirect
from .forms import ConsumptionForm, ConsumerForm
from calculator_python import calculator
import pandas as pd
from .models import Consumer, DiscountRule, ConsumerTypes
from django.contrib import messages




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


def consumer_list(request):
    consumers = Consumer.objects.all().select_related('discount_rule')

    consumer_type = request.GET.get('consumer_type')
    consumption_min = request.GET.get('consumption_min')
    consumption_max = request.GET.get('consumption_max')

    if consumer_type:
        consumers = consumers.filter(discount_rule__consumer_type=consumer_type)
    if consumption_min:
        consumers = consumers.filter(consumption__gte=consumption_min)
    if consumption_max:
        consumers = consumers.filter(consumption__lte=consumption_max)

    data = []
    for consumer in consumers:
        if consumer.discount_rule:
            monthly_savings = (
                consumer.consumption * consumer.distributor_tax *
                consumer.discount_rule.discount_value * consumer.discount_rule.cover_value
            )
            annual_savings = monthly_savings * 12
        else:
            monthly_savings = 0
            annual_savings = 0

        data.append({
            "consumer": consumer,
            "monthly_savings": round(monthly_savings, 2),
            "annual_savings": round(annual_savings, 2)
        })

    return render(request, 'list.html', {'consumers_data': data})

def add_consumer(request):
    discount_rule_choices = [(choice[0], choice[1]) for choice in ConsumerTypes.choices]
    if request.method == 'POST':
        form = ConsumerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consumidor adicionado com sucesso!')
            return redirect('consumer_list')
        else:
            print(form.errors)
            messages.error(request, 'O formulário contém erros. Por favor, corrija-os.')
    else:
        form = ConsumerForm()
    return render(request, 'add_consumer.html', {'form': form, 'discount_rule_choices': discount_rule_choices})


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
