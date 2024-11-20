"""
* Advinhe o Número
-> Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número. 
Algumas sugestões para o programa:

1. Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente a opção 
para sair do programa.
2. Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Ex: 1 a 10.
3. Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.
"""

import random

r1 = random.randint(1, 10)
x = 0

while r1 != x:
    x = int(input("Digite um valorS entre 1 e 10! \n"))
    if x > 0 and x <= 10:
        if r1 == x:
            print("Parabéns, você acertou!!")
        else:
            print("Você errou, tente de novo!")
    else:
        print("Digite um valor entre 1 e 10!")
