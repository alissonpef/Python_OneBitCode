gameSet = {"The witcher 3", "Red Dead Redepemtion 2", "Black Myth: Wukong", "The Last of Us: Part 1",
            "Days Gone", "Unchearted 4"}

# Não possibilita recuperar valores no set via slice
# True e o número 1 valem a mesma coisa
# Não permite repetir valores

# 1 - Buscar o tamanho do set
print(len(gameSet))

# 2 - True e o 1 equivalem a mesma coisa
gameSetExample = {"Fifa 25", True, 1, 299.90} 
print(gameSetExample)

# 3 - Adicionar item de outro set
gameSet.update(gameSetExample)
print(gameSet)

# 4 - Remover um item do set
gameSet.remove(True)
print(gameSet)
