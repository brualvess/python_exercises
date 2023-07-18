'''
É aniversário da Creuza e ela não sabe quantas velas colocar em cima do bolo. 
Problema: Ela sabe o ano em que nasceu, mas não sabe qual a idade dela.
'''

from datetime import date

def age_of_creuza():
    birth_year = int(input("Creuza, em que ano você nasceu ? "))
    current_year = date.today().year
    old = current_year - birth_year
    print("Você está complentando", old, "anos, então vamos colocar", old, "velas no bolo.")

age_of_creuza()
