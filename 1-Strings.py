"""
* Módulo de Strings
-> Escreva um módulo em python para tratar algumas strings
e que possua as seguintes funcionalidades:
1. Inverter uma string de trás pra frente.
2. Retornar apenas letras com índice par.
3. Retornar apenas letras com índice ímpar.
"""

from Exercise_1_aux import invert, even, odd

aux = input("Digite uma string: ")  
print("Escolha o que fazer: \n1 - Inverter uma string de trás pra frente.\n2 - Retornar apenas letras com índice par."
      "\n3 - Retornar apenas letras com índice ímpar.")
choice = int(input(">. "))

if choice == 1:
    invert(aux)
elif choice == 2:
    even(aux)
elif choice == 3:
    odd(aux)
else:
    print("Opção inválida!")