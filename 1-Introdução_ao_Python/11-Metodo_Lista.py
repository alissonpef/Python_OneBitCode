gameList = ["The witcher 3", "Red Dead Redepemtion 2", "Black Myth: Wukong", "The Last of Us: Part 1",
            "Days Gone", "Unchearted 4"]

# 1 - Tamanho da lista
print(len(gameList))

# 2 - Recupera um item da lista pelo índice
print(gameList.index("Days Gone"))

# 3 - Adiciona item ao final da lista
gameList.append("GTA V")
print(gameList)

# 4 - Ordena lista
gameList.sort()
print(gameList)

# 5 - Copia os itens de uma lista para outra
gameTeste = gameList.copy()
gameTeste.remove("Unchearted 4")
print(gameTeste)

# 6 - Remove todos os itens da lista
gameList.clear()
print(gameList)
