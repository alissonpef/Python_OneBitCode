import pprint #  Módulo para facilitar a visualização do print

gamesDict = {
  "fifa 24" : {
    "yearLaunch" : 2023,
    "classification" : 8.5,
    "genre": ["esporte", "família"]
  },
  "mario odyssey" : {
    "yearLaunch" : 2017,
    "classification" : 10.0,
    "genre": ["aventura", "3d"]
  },
  "donkey kong country" : {
    "yearLaunch" : 1996,
    "classification" : 9.5,
    "genre": ["aventura", "plataforma"]
  }
}

# print(dictJogos)
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

line = "="
print(line * 25)

# 1 - Buscando informação dentro de um dicionário
print(gamesDict["mario odyssey"]["genre"]) # Qual jogo eu quero, depois qual informação
print(line * 25)

# 2 - Adicionando novo item
gamesDict["mario odyssey"]["players"] = 1 
print(gamesDict['mario odyssey'])
print(line * 25)

# 3 - Excluindo um dicionário
del gamesDict["fifa 24"]
pp.pprint(gamesDict)
print(line * 25)
