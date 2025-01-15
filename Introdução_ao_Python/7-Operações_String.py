gameName = "The witcher"
gameVersion = "3"
line  = "="
gameDiscription = """
The Witcher 3 é um jogo no estilo de RPG mundo aberto.
Vale ressaltar que ele ganhou o premio de melhor jogo do ano de 2015
na TGA.
"""

# 1 - Concatenação de Strings
gameFullName = gameName + " " + gameVersion
print(gameFullName)

# 2 - Multiplicação de Strings
print(line * 25)

# 3 - Procura de uma palavra na String
print("The witcher" in gameName)
print("RPG" in gameDiscription)