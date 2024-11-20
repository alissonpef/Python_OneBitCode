"""
* Cálculo da Distância
-> Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
0,35 para viagens mais longas.
"""
distancia = float(input("Digite a distância que deseja percorrer em km: "))

if distancia <= 200:
    distancia *= 0.50
else:
    distancia *= 0.35

print(f"O preço da viagem ficou em R$: {distancia:.2f}.")

"""
* Aumento salário funcionário
-> Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
"""
salario = float(input("Digite o seu salário: "))

if salario >= 1250:
    salario *= 1.10
else:
    salario *= 1.15

print(f"O seu salário reajustado ficou em R$: {salario:.2f}")