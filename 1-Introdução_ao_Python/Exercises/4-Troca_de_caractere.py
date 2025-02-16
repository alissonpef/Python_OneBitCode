"""
Exercicio 3:
* Substituindo caractere repetido:
-> Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e 
troque os dois primeiros caracteres de cada string.
Ex:
abc xyz → xyc abz
"""

name1 = "abc"
name2 = "xyz"

print(name1 + " " + name2)
print(name2[:2] + name1[2:] + " " + name1[:2] + name2[2:])