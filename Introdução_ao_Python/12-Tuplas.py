gamesTuple = ("Horizon Zero Dawn", "Red Dead 2",
             "God of War", "Uncharted 4")
print(gamesTuple)
print(type(gamesTuple))

# - Não possibilita adicionar valores na tupla
# - Não possibilita remover valores na tupla
# - Não possibilita ordenar valores na tupla
# - Não permite repetir valores

line = "="
print(line * 25)

# 1 - Buscar os dois primeiros itens da lista
print(gamesTuple[:2]) # índice final -1
print(line * 25)

# 2 - Buscar o último item da lista
print(gamesTuple[-1])
print(line * 25)

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[:3])
print(line * 25)

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[1:4])
print(line * 25)

# 5- Recupera um item da tupla pelo índice
print(gamesTuple.index("Horizon Zero Dawn"))
print(line * 25)
