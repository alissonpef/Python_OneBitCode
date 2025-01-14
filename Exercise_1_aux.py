def invert(name):
    fullName = ""
    aux = ""
    for i in range(len(name)):
        aux = name[-1]
        name = name[:-1]
        fullName += aux
    print(f"A string invertida ficou: {fullName}")

def even(name):
    print(f"As letras com índice par ficaram: {name[::2]}")

def odd(name):
    print(f"As letras com índice ímpar ficaram: {name[1::2]}")
