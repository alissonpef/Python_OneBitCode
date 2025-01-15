# 1 - Função para imprimit Hello Word
def welcome():
    print("Hello Word!")

# 2 - Função para somar dois números
def sum():
    return(5 + 4)

# 3 - Função para cadastrar um jogo
def create_game():
    name = input("Digite o nome do jogo\n")
    yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
    gamePrice = float(input("Digite o preço do jogo\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\n"))
    print(f"{name} - R$ {gamePrice} - {yearLaunch} - {noteRating}")

# Chamadas da função
welcome()
sum()
create_game()