# 1 - Função para imprimit o nome completo
def full_name(fname, lname):
    print(f"{fname}  {lname}")

full_name("Alisson", "Pereira")

# 2 - Função para somar dois números
def sum(a, b):
    return(a + b)
print(sum(5, 4))

# 3 - Função com argumentos default
def address(country="Brasil"):
    print(f"Eu moro no {country}")
address()
address("Canadá")

# 4 - Avaliação do jogo
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo \\n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo\\n"))
rating_game(rating)