gameWitcher = {
    "name": "The witcher 3",
    "yearLaunch": 2015,
    "gamePrice": 149.90,
    "classificacao": 9.5,
    "genre": ["RPG", "ação"]
}

# 1 - Recuperando um elemento do dicionário
print(gameWitcher["genre"])
print(gameWitcher.get("gamePrice"))

# 2 - Buscando apenas as chaves
print(gameWitcher.keys())

# 3 - Buscando apenas os valores
print(gameWitcher.values())

# 4 - Retorna itens do dicionário como tupla de uma lista 
print(gameWitcher.items())

# 5 - Adicionando itens no dicionário
gameWitcher["Players"] = 2
print(gameWitcher)

# 6 - Atualizando itens no dicionário
gameWitcher.update({"Players": 1}) 

# 7 - Removendo item no dicionário
gameWitcher.pop("Players")
print(gameWitcher)