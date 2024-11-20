"""
* Conta letras maiúsculas e minúsculas:
-> Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.
"""

palavra = input("Digita a palavra a ser verificada: ")
numeroLetras = len(palavra)
cont = 0
contMaisculo = 0
contMinusculo = 0
    
while numeroLetras != 0:
    char = palavra[cont]
    charMaisculo = palavra[cont].upper() # Retorna a string em maiúsculo
    charMinusculo = palavra[cont].lower() # Retorna a string em minúsculo
    
    if char == charMaisculo:
        contMaisculo += 1
    if char == charMinusculo:
        contMinusculo +=  1
    
    numeroLetras -= 1
    cont += 1

print(f"A palavra {palavra} tem {contMaisculo} letras maisculas e {contMinusculo} minusculas.")

"""
* Lista números pares e ímpares de uma lista
-> Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
"""

tam = int(input("Digite o tamanho da lista: "))

lista = []
par = []
impar = []

for i in range(tam):
    numLista = int(input("Digite o número: "))
    lista.append(numLista)

for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"\nOs números pares são: {par}")
print(f"Os números impares são: {impar}")