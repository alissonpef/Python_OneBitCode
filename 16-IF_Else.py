name = input("Digite o nome do game: ")
yearLaunch = int(input("Digite o ano de lançamento do jogo: "))
classification = float(input("Digite a nota do jogo: "))

if classification > 8.0 or yearLaunch > 2015 & yearLaunch < 2023:
    print(f"O jogo {name} é um ótimo jogo. Recomendo jogá-lo!")
else:
    print(f"O jogo {name} não é um bom jogo. Não recomendo jogá-lo!")
