name = input("Qual seu nome? \n")
"""
Arquivos:
1- r - Leitura
2- w - Escrita
3- a - Append
"""

# Alternativa 1
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# Alternativa 2
with open("dados/names.txt", "a") as file: # as faz com que quando chamamos file, realizamos o with open...
    file.write(f"{name}\n")