from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculator/', views.calculator_view, name='calculator'),
    path('import/', views.importar_xlsx, name='importar_xlsx'),

]
