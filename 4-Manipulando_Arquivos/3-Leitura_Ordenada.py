names = []

with open("dados/names.txt", "r", encoding="UTF-8") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names): # Ordena os nomes
    print(f"Olá, {name}")
