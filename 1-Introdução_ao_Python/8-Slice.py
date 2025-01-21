gameName = "The witcher 3"
gameDiscription = """
The Witcher 3 é um jogo no estilo de RPG mundo aberto.
Vale ressaltar que ele ganhou o premio de melhor jogo do ano de 2015
na TGA.
"""

# string[início:fim] - índice começa com 0 | índice final -1

# 1- Busque toda string a partir da primeira posição
print(gameName[0:])

# 2 - Busque toda string até a última posição
print(gameName[:12])

# 3 - Busque toda string da quinta até a última posição
print(gameName[4:])

"""
string[início:fim:passo] - índice começa com 0 | índice final -1 | 
passo - determina o incremento. Por padrão esse número é o 1.
"""

# 4 -Busque toda a string de 2 em 2 caracteres.
print(gameName[::2])

# 5 - Imprime os caracteres nos índices ímpares
print(gameName[1::2])

# 6 - Inverta uma string de trás pra frente
print(gameName[::-1])