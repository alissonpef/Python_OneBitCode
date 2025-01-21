from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Conta itens de uma lista
fruits = ["Maçã", "Banana", "Uva", "Pêra", "Uva", "Maçã", "Uva", "Banana"]
print(fruits)
print(Counter(fruits))

# 2 - Utilizando uma tupla nomeada
game = namedtuple('Game', ['name', 'price', 'note'])  # Ajuste na capitalização de 'Game' (boa prática)
g1 = game("Fifa 23", 90.50, 8.5)
g2 = game("Resident Evil 4", 300.00, 10.0)
print(g1)
print(g2)

# 3 - Ordenando dicionários
students = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}  # Corrigido para 'students'
sorted_students = sorted(students.items(), key=itemgetter(0))  # Variável mais descritiva
print(students)
print(sorted_students)

# 4 - Utilizando fila ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)
