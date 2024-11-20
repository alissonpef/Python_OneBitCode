"""
* Antecessor e Sucessor de um número
-> Escreva um programa em Python que leia um número e represente o número 
antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.
"""

num = int(input("Digite um número: "))
ant = num - 1
suc = num + 1
print(f"O antecessor do número {num} é {ant}. \nO sucessor do número {num} é o {suc}.")
# print(f"O antecessor do número {num} é {num -1}. \nO sucessor do número {num} é o {num +1}.")

"""
* Média de 4 notas
-> Escreva um programa em Python que leia quatro números e calcule a média entre esses números.
"""

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
num4 = float(input("Digite o quarto número: "))
media = (num1 + num2 + num3 + num4)/4

print(f"A média dos quatro números é: {media}")
