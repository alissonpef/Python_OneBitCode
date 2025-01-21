"""
Exercicio 8:
* Tabuada:
-> Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário.
"""

num = int(input("Digite o número que deseja a tabuada: "))
begin = int(input("Digite a partir de que número deseja iniciar: "))
end = int(input("Digite a partir de que número deseja finalizar: "))
sum = 0

for i in range(end - begin + 1):
    sum = num * begin
    print(f"{num} * {begin} = {sum}")
    begin+= 1