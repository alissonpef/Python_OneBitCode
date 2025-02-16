
with open("dados/names.txt", "r", encoding="UTF-8") as file: # UTF-8 ele entender caracteres especiais
    for line in file:
        # print(f"Olá {line}")
        print(f"Olá {line.rstrip()}") # Remove linha vazia
