def wellcome(): # Definindo uma função
    print("Hello World")

def sum():
    return 1 + 1

def create_game():
    name = input("Digite o nome do jogo: ")
    yearLaunch = int(input("Digite o ano de lançamento: "))
    gamePrice = float(input("Digite o preço do jogo: "))
    noteRating = float(input("Digite a nota de avaliação do jogo: "))
    print(name)
    print(yearLaunch)
    print(gamePrice)
    print(noteRating)

line = "="
print(line * 25)

wellcome() # Chamando a função
print(line * 25)

print(sum()) # Chamando a função
print(line * 25)

create_game() # Chamando a função
print(line * 25)