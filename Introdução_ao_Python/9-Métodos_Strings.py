gameName = "The witcher 3"
gameDiscription = """
The Witcher 3 é um jogo no estilo de RPG mundo aberto,
vale ressaltar que ele ganhou o premio de melhor jogo do ano de 2015,
na TGA.
"""

print(gameName.upper()) # Retorna tudo em Maiúsculo
print(gameName.lower()) # Retorna tudo em Minúsculo
print(gameName.title()) # Retorna a primeira letra em maiúsculo
print(gameName.capitalize()) # Retorna a primeira letra em maiúsculo
print(gameName.center(30, "-")) # Retorna a string centralizada com caractere de preenchimento
print(gameName.find("h")) # Retorna a posição de um determinado caractere
print(gameDiscription.find("e")) # Conta quantos caracteres tem em determinada variável
print(gameName.replace("3", "2")) # Troca uma string por outra
print(gameDiscription.split(",")) # Divide os elementos com base no caractere