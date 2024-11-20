gamesList = ["Fifa 24", "Horizon Zero Dawn", "Red Dead 2",
            "God of War", "Uncharted 4"]

line = "="
print(line * 25)

# 1 - Tamanho da lista
print(len(gamesList))
print(line * 25)

# 2 - Recuperar um item da lista pelo índice
print(gamesList.index("God of War")) # Retorna o índice do God of War
print(line * 25)

# 3 - Adiciona item ao final da lista
gamesList.append("GTA V")
print(gamesList)
print(line * 25)

# 4 - Ordena lista
gamesList.sort()
# gamesList.reverse()
print(gamesList)
print(line * 25)

# 5 - Copia os itens de uma lista para outra
gamesReset = gamesList.copy()
gamesReset.remove("Fifa 24")
gamesReset.remove("GTA V")
print(gamesReset)
print(line * 25)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)
print(line * 25)
