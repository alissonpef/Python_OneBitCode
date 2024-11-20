"""
1 - Liste valores de 0 a 10 que sejam menores do que 4.
for i in range(10):
    if i <4:
        print(i)
"""

"""
nova_lista = [expressão for item in iterável if condição]

1. expressão: O valor ou cálculo que você quer adicionar à nova lista. Pode ser um item da lista original (item), 
uma transformação desse item, ou uma combinação de itens.
2. item: Uma variável que representa cada elemento do iterável na iteração.
3. iterável: A lista, tupla, ou outro tipo de coleção que você está percorrendo.
4. condição (opcional): Um teste lógico que filtra quais itens são incluídos na nova lista. Se a condição é verdadeira, 
o item é incluído; se é falsa, é descartado.
"""

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = ["Mario Odyssey", "Donkey Kong Country", "Luigi's mansion", "Kirby"]

newList = [x for x in gamesList if "a" in x] # Jogos que tenham a letra "a"
print(newList)

gamesFinished = [x for x in gamesList if x != "Kirby"] # Demais jogos menos o Kirby
print(gamesFinished)
