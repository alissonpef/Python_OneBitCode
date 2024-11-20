line = "="
print(line * 25)

# 1 - Crie uma função que receba dois argumentos: primeiro nome e o último nome. 
def full_name(fname, lname): # Definindo uma função
    print(f"{fname} {lname}")
full_name("Alisson", "Ferreira") # Chamando a função
print(line * 25)

# 2 - Crie uma função que some dois números via argumentos.
def sum(a, b): # Definindo uma função
    print(a + b)
sum(20, 10) # Chamando a função
print(line * 25)

# 3 - Argumento default numa função.
def address(country="Irlanda"):
    print(f"Eu moro no {country}")
address() # Chamando a função
address("Brasil") # Chamando a função
print(line * 25)

# 4 - Avaliação de um jogo.
def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo: ")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo \n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo\n")) # Definindo a quantidade de avaliações
rating_game(rating) # Chamando a função