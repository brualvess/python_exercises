'''
Creuza vai viajar e precisa comprar dólares
Problema: Ela têm o dinheiro em reais, e precisa saber quantos doláres irá poder comprar. Considere que o dólar está 4.87
'''
def convert_dollar():
    value_in_real = float(input("Informe a quantidade que você possui em reais R$ "))
    dolar = value_in_real / 4.87
    if dolar <= 1:
        print(f'Você poderá comprar {dolar:.2f} dólar')
    else:
        print(f'Você poderá comprar {dolar:.2f} dólares')


convert_dollar()