import math

# 1 - Acessar o número de Pi
print(math.pi)
print(f"{math.pi:.2f}") # Formatando em duas casas decimais

# 2 - Acessar o número de Euler
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arredondando números para cima e para baixo
num1 = 10.3 
print(math.ceil(num1)) # Arredonda para baixo
print(math.floor(num1)) # Arredonda para cima

# 4 - Fatorial de um número 
num2 = 7
print(math.factorial(num2))

# 5 - Potência de números
print(math.pow(5,5)) # equivale a 5 ** 5

# 6 - Raiz quadrada 
print(math.sqrt(169)) 

# 7 - Maior denominador comum - Reduzir frações
mdc = math.gcd(25, 120)
print(mdc)

# 8 - Logaritmo
print(math.log(10))
print(math.log(10, 3))