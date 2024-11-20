gameName = "Fifa 24"
num = "0123456789"
gameDescription = """
Fifa 24 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar 
localmente ou online.
"""

# string[início:fim] - índice começa em 0 | índice final -1

# 1 - Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a última posição
print(gameName[:7])

# 3 - Busque toda string da terceira até a última posição
print(gameName[2:])

"""
string[início:fim:passo] - índice começa com 0 | índice final -1 | 
passo - determina o incremento. Por padrão esse número é o 1
"""

# 4 - Busque toda string de 2 em 2 caracteres
print(num[::2])

# 5 - Imprime os caracteres nos índices ímpares
print(num[1::2])

# 6 - Inverta uma string de trás pra frente
print(num[::-1])

