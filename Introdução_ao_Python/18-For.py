gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1 - Iterando valores de uma lista, ou seja, printa todos os valores da lista
for i in gamesList:
    print(i)
line = "="
print(line * 25)

# 2 - Quando a condição for atendida, o Loop será encerrado
for i in gamesList:
    if i == "God of War":
        break
    print(i)
print(line * 25)

# 3 - Quando a condição for atendida, o Loop vai para a próxima iteração, ou seja, pula o desejado
for i in gamesList:
    if i == "God of War":
        continue
    print(i)
print(line * 25)

# 3 - Avaliação Jogo
gameName = input("Digite o nome do jogo: ")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo: "))

sum = 0
for i in range(gameRating): # Range define até aonde o laço vai, ou seja, um valor limite
    note = float(input("Digite a nota para o jogo: "))
    sum += note # sum = sum + note
print(f"Média de avaliação do jogo {gameName} é: {sum/gameRating :.2f}")

