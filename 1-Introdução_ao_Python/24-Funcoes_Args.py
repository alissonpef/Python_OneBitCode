"""
*args: Utilizamos ele quando não temos a certeza de quantos argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

*kwargs: Além dos valores, podemos passar também as respectivas chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""

# 1 - Soma de Números
def sum(*num):
    sum_total = 0
    for n in num:  # Num é uma tupla
        sum_total = sum_total + n
    print(f"Soma é: {sum_total}")

sum(7)
sum(8, 7)
sum(4, 5, 9)
sum(6, 8, 3, 1)

# 2 - Apresentação de Cursos
def presentation(**data):
    for key, value in data.items():  # Data é passado como um dicionário
        print(f"{key} - {value}")

print("###Curso###")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Machine Learning", category="IA", level="Avançado")
