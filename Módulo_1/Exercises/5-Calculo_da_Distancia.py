"""
Exercicio 5:
* Cálculo da distanceância:
-> Escreva um programa que pergunte a distancia que um passageiro deseja percorrer em km. Calcule o preço da passagem, 
cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.
"""

distance = int(input("Quantos km você deseja percorrer? \n"))

if distance <= 200:
    ticket = 0.50 * distance
elif distance > 200:
    ticket = 0.25 * distance
else:
    print("Valor incorreto!")

print(f"O valor da passagem ficou em {ticket} reais!")