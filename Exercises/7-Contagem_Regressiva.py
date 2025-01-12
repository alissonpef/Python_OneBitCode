"""
Exercicio 7:
* Contagem Regressiva:
-> Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve 
imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
"""
cont = 10
for i in range(11):
    print(cont)
    cont += -1
    if cont == -1:
        print("beep")
    