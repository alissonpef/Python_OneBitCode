num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Aritméticos
sum = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2 # Resto da divisão
exp = num1 ** num2

print("\nOperadores Aritméticos")
print(f"A soma de {num1} com {num2} é: {sum}")
print(f"A subtração de {num1} com {num2} é: {sub}")
print(f"A divisão de {num1} com {num2} é: {div}")
print(f"A multiplicação de {num1} com {num2} é: {mult}")
print(f"O resto da divisão de {num1} com {num2} é: {mod}")
print(f"A exponencial de {num1} com {num2} é: {exp}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print("\nOperadores de Comparação:")
print(f"O {num1} é maior que o {num2}? {bigger}")
print(f"O {num1} é menor que o {num2}? {smaller}")
print(f"O {num1} é igual ao {num2}? {equal}")
print(f"O {num1} é diferente do {num2}? {different}")
print(f"O {num1} é maior ou igual ao {num2}? {bigger_equal}")
print(f"O {num1} é menor ou igual ao {num2}? {smaller_equal}")

# Atribuição
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1