print("Lembre-se que para encerrar o programa, deve digitar -1\n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0 # Inicia em 0 para não dar erro ao não colocar nenhuma nota

gameName = input("Digite o nome do jogo: ")

while(rating != -1):
    rating = float(input("Informe a nota do jogo\n"))
    if(rating != - 1):
        totalRating += rating
        qtdRating += 1
        average = totalRating / qtdRating
        
print(f"Média das avaliações do jogo {gameName} é: {average:.2f}")