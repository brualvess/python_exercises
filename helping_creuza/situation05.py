'''
Depois de comprar muita muamba e ter os 60% a pagar de imposto, creuza ficou sem dinheiro e teve que pegar um empréstimo no banco
Problema: Ela precisa de ajuda para saber quanto vai pagar em cada parcela. Considere 20% de juros
'''
def loan_in_the_bank():
    loan_amount = float(input('Qual valor você quer pegar R$ '))
    plots = int(input('Em quantas parcelas ? '))
    interest = 0.20 * loan_amount
    total_value = (interest + loan_amount) / plots

    print(f'Valor do empréstimo R${loan_amount:.2f}\n Valor do juros R${interest:.2f}\n Quantidade de parcelas: {plots}\n Você vai pagar {plots} parcelas de R${total_value:.2f}')

loan_in_the_bank()


