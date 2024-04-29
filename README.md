# Sistema de Energia Solar

## Descrição do Projeto
Este projeto consiste em uma aplicação web desenvolvida com Django, HTML, e CSS para uma empresa de assinatura de energia. A aplicação inclui uma calculadora de economia que estima a economia anual e mensal para diferentes tipos de tarifas energéticas, baseando-se em diversos parâmetros de consumo.

## Tecnologias Utilizadas
- **Django**: Utilizado para a construção do backend e integração com o frontend.
- **HTML**: Estruturação das páginas da web.
- **CSS**: Estilização e design das páginas da web.

## Etapas do Projeto

### Etapa 1: Desenvolvimento da Calculadora
#### Requisitos:
- Implementar a calculadora no arquivo `calculator_python.py` dentro da função `calculator()`.
- Integrar a calculadora com uma interface desenvolvida com Django, HTML e CSS.
- Executar todos os testes do arquivo `calculator_python.py` sem erros.

#### Entradas da Calculadora:
- Consumo de energia elétrica dos últimos três meses.
- Valor da tarifa da distribuidora.
- Tipo de tarifa (Comercial, Residencial, Industrial).

#### Saídas da Calculadora:
- Economia Anual.
- Economia Mensal.
- Desconto Aplicado.

#### Descontos e Coberturas:
- Descontos e coberturas são calculados com base no consumo médio e tipo de tarifa conforme tabelas fornecidas.

### Etapa 2: Armazenamento de Dados e Cálculo Avançado
#### Requisitos:
- Armazenar dados de consumidores e suas informações de consumo no banco de dados.
- Armazenar regras de desconto no banco de dados e associá-las a cada consumidor.
- Calcular a economia baseada nos atributos do consumidor.
- Listar consumidores e suas economias em uma tabela.

### Etapa 3: Aprimoramento da Aplicação Web
#### Requisitos:
- Permitir filtragem na tabela por tipo de consumidor e intervalo de consumo.
- Incluir consumidores por meio de formulário com campos automáticos preenchidos via API do ViaCEP.
- Validar o documento do consumidor de acordo com o tipo.


