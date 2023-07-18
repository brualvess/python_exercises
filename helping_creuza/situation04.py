'''
Creuza voltou de viagem e comprou muita muamba
Problema: Ela quer saber o valor a pagar do imposto de mercadoria. Considere que a porcentagem do imposto é 60% 
'''

def commodity_tax():
    product_value = float(input('Qual o valor do produto ? '))
    tax = (product_value * 60) / 100
    print(f'O imposto a ser pago é R$ {tax:.2f}')

commodity_tax()


