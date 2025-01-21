gameTuple = ("The witcher 3", "Red Dead Redepemtion 2", "Black Myth: Wukong", "The Last of Us: Part 1",
            "Days Gone", "Unchearted 4")

# Não possibilita adicionar valores na tupla
# Não possibilita remover valores na tupla
# Não possibilita ordenar valores na tupla

# 1 - Busque itens da lista até determinada posição
print(gameTuple[:3])

# 2 - Busque o último item da lista
print(gameTuple[-1])

# 3 - Busca jogos de uma posição em diante
print(gameTuple[3:])

# 4 - Recuperar um item da tupla pelo índice
print(gameTuple.index("Days Gone"))
