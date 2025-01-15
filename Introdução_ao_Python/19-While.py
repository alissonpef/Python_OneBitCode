gameName = input("Digite o nome do jogo: ")
rating = 0
qtdRating = 0
totalRating = 0
avarage = 0

while rating != -1:
    rating = float(input("Digite a nota do jogo: "))
    if (rating != -1):
        qtdRating += 1
        totalRating += rating
        avarage = totalRating / qtdRating

print(f"A nota do jogo {gameName} é {avarage:.2f}!")
