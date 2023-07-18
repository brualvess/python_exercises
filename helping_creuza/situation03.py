'''
Creuza chegou nos Estados Unidos e a temperatura de medida ultilizada lá não é celsius e sim fahrenheit
Problema: Seu celular está com a temperatura em fahrenheit, e ela quer saber quantos graus seria no Brasil
'''
def degree_conversion():
    degree_fahrenheit = float(input('Qual é a temperatura aqui ? '))
    degree_celsius = (degree_fahrenheit - 32) / 1.8
    print(f'A temperatura no Brasil estaria {degree_celsius:.2f}°C')

degree_conversion()