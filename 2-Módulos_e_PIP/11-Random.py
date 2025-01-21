import random

# 1 - Seleciona valor aleatório de uma lista
list1 = [7, 6, 4, 3, 2, 1]
print("Valor aleatório da lista:", random.choice(list1))

# 2 - Gera número aleatório em um intervalo de valores
r1 = random.randint(5, 12)
print("Número aleatório entre 5 e 12:", r1)

# 3 - Seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name)
print("Caractere aleatório da string:", r2)

# 4 - Selecionando mais de um valor aleatório
# Sintaxe: random.sample(sequencia, tamanho)
print("Dois valores aleatórios da lista:", random.sample(list1, 2))
print("Três valores aleatórios da lista:", random.sample(list1, 3))

s = "Olá mundo"
print("Dois caracteres aleatórios da string:", random.sample(s, 2))
