# [adicao_a_lista for váriavel_que_muda in iterable if condition == True]

# 1 - Liste os valores de 0 a 10 que sejam menores que 4
# for i in range(10):
#     if (i < 4):
#         print(i)
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# 2 - Jogos que possuam a letra a
gameList = ["The witcher 3", "Red Dead Redepemtion 2", "Black Myth: Wukong", "The Last of Us: Part 1",
            "Days Gone", "Unchearted 4"]

newList = [x for x in gameList if "a" in x]
print(newList)

# 3 - Jogos que eu zerei
gamesFinished = [x for x in gameList if x != "Days Gone"] 
print(gamesFinished)



