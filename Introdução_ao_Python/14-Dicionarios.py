gameFifa = {
    "price": 90.55, # "Chave": Valores
    "yearLaunch": 2023,
    "version": 2024,
    "classification": 8.5,
    "genre": ["esporte", "família"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

line = "="
print(line * 25)

# 1 - Recuperando um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))
print(line * 25)

# 2 - Buscando apenas as chaves
print(gameFifa.keys())
print(line * 25)

# 3 - Buscando apenas os valores
print(gameFifa.values())
print(line * 25)

# 4 - Busca itens do dicionário com chave e valor
print(gameFifa.items())
print(line * 25)

# 5 - Adicionando itens no dicionário
gameFifa["players"] = 2
print(gameFifa)
print(line * 25)

# 6 - Atualizando itens no dicionário
gameFifa.update({"players": 1})
print(gameFifa)
print(line * 25)

# 7 - Removendo item no dicionário
gameFifa.pop("players")
print(gameFifa)
print(line * 25)
