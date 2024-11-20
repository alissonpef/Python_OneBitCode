# 1 - Função de potência de um número
power = lambda num: num ** 2

# 2 - Função para verificar se um número é par
pair = lambda x: x%2==0

# 3 - Função para dividir dois números
divNum = lambda x,y : x/y

# 4 - Função para inverter uma string
reverse = lambda s: s[::-1]

line = "="
print(line * 25)

print(power(5))
print(line * 25)

print(power(9))
print(line * 25)

print(pair(27))
print(line * 25)

print(pair(30))
print(line * 25)

print(divNum(10,2))
print(line * 25)

print(divNum(7,2))
print(line * 25)

print(reverse("Função"))
print(line * 25)

print(reverse("Tecnologia"))
