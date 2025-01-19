import statistics

# 1 - Aplicar a média
print(statistics.mean([3,2,3,8,9]))

# 2 - Aplicar a mediana
print(statistics.median([1,2,3,8,9]))
print(statistics.median([1,2,3,7,8,9])) # Média dos dois números centrais

# 3 - Aplicar a moda # O que mais se repete
print(statistics.mode([2,5,3,2,8,3,9,4,2,5,6]))

# Aplicar o desvio padrão
"""
Medida de dispersão do conjunto, ou seja, uma medida  que indica quão uniformes são os dados do conjunto.
- Quanto mais próximo de 0, significa que os dados do conjunto estão menos dispersos
"""

print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]))