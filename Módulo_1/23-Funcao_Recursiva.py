"""
1 -> 1
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))

number = int(input("Digite o número para fatorial: "))
print(f"O fatorial de {number} é: {factorial(number)}")
