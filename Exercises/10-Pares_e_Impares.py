"""
Exercicio 10:
* Lista números pares e ímpares de uma lista:
-> Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
"""

def check_number(num):
    par = num[::2]
    impar = num[1::2]
    return par, impar


par, impar = check_number([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(f"Lista de números pares{par} e números impares{impar}")