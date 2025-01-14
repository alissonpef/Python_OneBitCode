import pprint

gamesDict = {
    "The witcher 3": {
        "yearLaunch": 2015,
        "classificacao": 9.5,
        "genre": ["RPG", "ação"],
    },
    "mario odyssey": {
        "yearLaunch": 2017,
        "classification": 10.0,
        "genre": ["aventura", "3d"],
    },
    "donkey kong country": {
        "yearLaunch": 1996,
        "classification": 9.5,
        "genre": ["aventura", "plataforma"],
    },
}

print(gamesDict )
print(25 * "=")

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)
print(25 * "=")

# 1 - Buscando informação dentro de um dicionário
print(gamesDict["mario odyssey"]["genre"])
print(25 * "=")

# 2 - Adicionando novo item
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict["mario odyssey"])
print(25 * "=")

# 3 - Excluindo um dicionário
del gamesDict["The witcher 3"]
pp.pprint(gamesDict)