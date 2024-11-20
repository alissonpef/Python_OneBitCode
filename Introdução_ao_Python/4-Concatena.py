name = input("Digite o nome do jogo: \n")
yearLaunch = int(input("Digite o ano de lançamento: \n"))
gamePrice = float(input("Digite o preço do jogo: \n"))
planIncluded = bool(input("Digite se ele pertence a algum plano? \n"))


print("\n###Dados do Jogo###")
print("===================")

# Alternativa 1
# print("Nome do Jogo: ", name)
# print("Ano de lançamento do Jogo: ", yearLaunch)
# print("Preço do Jogo: ", gamePrice)
# print("Está incluído no plano? ", planIncluded)

# Alternativa 2
# print("Nome do Jogo: ", name, "\nAno de lançamento do Jogo: ", yearLaunch,
#       "\nPreço do Jogo: ", gamePrice, "\nEstá incluído no plano? ", planIncluded)

# Alternativa 3
print(f"Nome do Jogo:  {name} \nAno de lançamento do Jogo:  {yearLaunch}" 
      f"\nPreço do Jogo:  {gamePrice}  \nEstá incluído no plano?  {planIncluded}")
