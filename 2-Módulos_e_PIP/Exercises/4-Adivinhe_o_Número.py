"""
* Advinhe o Número
-> Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número.
1. Utilizar um laço de repetição para que o programa execute até que o usuário informe um número referente à 
opção para sair do programa.
2. Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Exemplo: 1 a 10.
3. Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.
"""
import random

num = random.randint(0, 10)
lista = []
done = False

while not done:
    aux = int(input("Digite um número entre 0 a 10: "))
    if num == aux:
        print("Parabéns, você ganhou!")
        done = True
    elif num != aux:
        lista.append(aux)
        print(f"O(s) números {lista} não são o número aleatório, tente novamente!")
    else:
        print("Opção inválida!")