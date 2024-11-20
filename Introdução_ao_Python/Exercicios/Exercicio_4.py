"""
* Contagem Regressiva:
-> Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
"""
import winsound

cont = 11 # cont - 1
for i in range(11):
    cont -= 1
    print(cont)
winsound.Beep(2500, 500)

"""
* Tabuada:
Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário.
"""

num = int(input("\nDigite o número desejado: "))
inicio = int(input("Número que inicia a tabuada: "))
fim = int(input("Até o número: "))
print("\n")

while inicio <= fim:
    print(f"Tabuada do {num} x {inicio} = {num * inicio}")
    inicio += 1
