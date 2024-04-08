from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculator/', views.calculator_view, name='calculator'),
    path('import/', views.importar_xlsx, name='importar_xlsx'),
    path('consumers/', views.consumer_list, name='consumer_list'),
    path('add_consumer/', views.add_consumer, name='add_consumer')

]
