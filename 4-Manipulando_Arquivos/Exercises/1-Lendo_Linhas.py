"""
Exercicio 1:
* Lendo n linhas de um arquivo:
-> Escreva um programa Python para ler as primeiras n linhas de um arquivo
1. O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.
"""

def read(name, num):
    with open(name, "r", encoding="UTF-8") as file:
        for _ in range(num):
            print(f"Olá {file.readline().rstrip()}")

# name = input("Digite o nome do arquivo desejado: ")
# num = int(input("Digite o número de linhas desejadas: "))
read("dados/names.txt", 3)