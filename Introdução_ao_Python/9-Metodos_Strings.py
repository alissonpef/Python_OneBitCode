gameName = "Fifa 24"
gameDescription = """
Fifa 24 é um jogo de futebol
desenvolvido pela EA Sports,
e que possibilita jogar 
localmente ou online.
"""

print(gameName.upper()) # Retorna a string em maiúsculo
print(gameName.lower()) # Retorna a string em minúsculo
print(gameName.capitalize()) # Apenas primeira letra em maiúscula
print(gameName.title()) # Apenas primeira letra em maiúscula
print(gameName.center(21, '-')) # Retorna a string centralizada com caractere de preenchimento
print(gameName.find("f")) # Retorna a posição de determinado caractere
print(gameDescription.count('a')) # Conta quantos caracteres 
print(gameDescription.count('A')) # Conta quantos caracteres 
print(gameDescription.replace("Fifa", "Pes")) # Altera um elemento por outro
print(gameDescription.split(',')) # Quebra o texto cada vez que ter um determinado elemento