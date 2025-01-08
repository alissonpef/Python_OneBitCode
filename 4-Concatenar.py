name = input("Ente the name of the game: ")  # input always returns string
yearLaunch = int(input("Enter the year the game was released: "))
gamePrice = float(input("Enter the price of the game: "))
planIncluded = input("Is this included in any plan? ")

print("##### Dados do Jogo #####")
print("====================")
# Alternativa 1
print("Nome do Jogo:", name, "\nAno de lançamento:", yearLaunch,
      "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço?", planIncluded)
print("====================")
# Alternativa 3
print(
    f"Nome do Jogo: {name} \nAno Lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nEstá incluso no serviço? {planIncluded}"
)
