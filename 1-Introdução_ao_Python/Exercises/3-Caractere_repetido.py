"""
Exercicio 3:
* Substituindo caractere repetido:
-> Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu 
primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere.
Ex:
fifa 23 → fi#a 23
restart→ resta#t
"""

name = "teste"
position = name.find("e") + 1
x = name[:position] # Índice final - -1
y = name[position:]
change = y.replace("e", "$")
print(x + change)