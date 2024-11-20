"""
args - Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""

line = "="
print(line * 25)

# 1 - Soma de números
def sum(*num): # Definindo uma função
    sum_total = 0
    
    for n in num:
        sum_total = sum_total + n

    print(f"Soma é: {sum_total}")
    
sum(7)
print(line * 25)

sum(8, 7)
print(line * 25)

sum(4, 5, 9)
print(line * 25)

sum(6, 8, 3, 1)
print(line * 25)

# 2 - Apresentação de um curso
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("######Curso######")
presentation(name="Python", category="Backend", level="Iniciante")