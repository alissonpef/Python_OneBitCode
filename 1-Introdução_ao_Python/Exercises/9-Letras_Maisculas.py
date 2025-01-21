"""
Exercicio 9:
* Conta letras maiúsculas e minúsculas:
-> Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.
"""

word = input("Digite uma palavra: ")
aux = word.upper()

def check_word (word, aux):
    maiscula = 0
    minuscula = 0
    for i in range(len(word)):
        aux2 = aux[i:i+1]
        aux3 = word[i:i+1]
        if aux2 == aux3:
            maiscula += 1
        else:
            minuscula += 1
    return maiscula, minuscula

maiscula, minuscula = check_word(word, aux)
print(f"A palavra {word} tem {maiscula} maisculas e {minuscula} minuscula.")