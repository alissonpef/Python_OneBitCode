"""
* Módulo de strings
-> Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

1. Inverter uma string de trás pra frente.
2. Retornar apenas letras com índice par.
3. Retornar apenas letras com índice ímpar.
"""

import Strings

string = input("Digita a String desejada: ")

print(f"A String invertida fica: {Strings.inverte(string)}")
print(f"Somente as Strings pares: {Strings.par(string)}")
print(f"Somente as Strings impares: {Strings.impar(string)}")