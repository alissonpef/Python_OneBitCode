import math

# 1 - Acessar o número de Pi
print(math.pi)
print(f"{math.pi:.2f}")

# 2 - Acessar o número de Euler
print(math.e)
print(f"{math.e:.2f}")

# 3 - Arredondando números para cima e para baixo
num1 = 10.4
print(math.ceil(num1))
print(math.floor(num1))

# 5 - Fatorial de um número 
num2 = 7
print(math.factorial(num2))

# 6 - Potênciação de números
print(math.pow(5,5)) # equivale a 5 ** 5

# 7 - Raiz quadrada 
print(math.sqrt(169)) 

# 8 - Logaritmo
print(math.log(10))
print(math.log(10, 3))

# 9 - Maior denominador comum - Reduzir frações
mdc = math.gcd(25, 120)
print(mdc)
