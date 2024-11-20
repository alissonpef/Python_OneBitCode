gamesSet = {"Horizon Zero Dawn", "Red Dead 2",
             "God of War", "Uncharted 4"}
print(gamesSet)

# - Não possibilita recuperar valores no set via slice
# - Não permite repetir valores

line = "="
print(line * 25)

# 1 - Buscar o tamanho do Set
print(len(gamesSet))
print(line * 25)

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Horizon Zero Dawn", True, 1, 90.50} 
print(exampleSet)
print(line * 25)

# 3 - Adicionando item de outro set
gamesSet.update(exampleSet)
print(gamesSet)
print(line * 25)

# 4 - Adicionando item no set
gamesSet.add("Resident Evil 4")
print(gamesSet)
print(line * 25)

# 5 - Remove um item no set
gamesSet.remove(True)
gamesSet.remove(90.5)
print(gamesSet)
print(line * 25)

