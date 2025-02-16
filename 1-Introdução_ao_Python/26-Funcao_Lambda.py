# 1 - Função de potência de número
power = lambda num: num**2

# 2 - Função que verifica se o número é par

pair = lambda x: x % 2 == 0

# 1 - Função que divide um número por outro
divNum = lambda x, y: x / y

# 4 - Função que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(pair(27))
print(pair(30))
print(divNum(10, 2))
print(divNum(7, 2))
print(reverse("Função"))
