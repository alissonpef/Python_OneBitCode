"""
Exercicio 5:
* Aumento salaryário funcionário:
-> Escreva um programa que pergunte o salaryário do funcionário e calcule o valor do aumento. Para salários superiores 
a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""

salary = int(input("Qual é o seu sálario? \n"))

if salary <= 1250:
    increase = 0.15 * salary
elif salary > 1250:
    increase = 0.10 * salary
else:
    print("Valor incorreto!")

print(f"O aumento do seu sálario ficou em {increase} reais!")