gameList = ["The witcher 3", "Red Dead Redepemtion 2", "Black Myth: Wukong", "The Last of Us: Part 1",
            "Days Gone", "Unchearted 4"]

# 1 - Iterando valores de uma lista
for i in gameList:
    print(i)
print(25 * "=")

# 2 - Quando a condição for atendida, o loop será encerrado
for i in gameList:
    if i == "Black Myth: Wukong":
        break
    print(i)
print(25 * "=")

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
for i in gameList:
    if i == "Black Myth: Wukong":
        continue
    print(i)
print(25 * "=")

# 4 - Avaliação Jogo
gameName = input("Digite o nome do jogo: ")
gameClassification = int(input("Digite quantas notas o jogo terá: "))

sum = 0
for i in range(gameClassification):
    note = float(input(f"Digite a {i + 1} nota: "))
    sum += note
    
print(f"A nota do jogo {gameName} ficou em {sum/gameClassification}")