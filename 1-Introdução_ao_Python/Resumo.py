"""
git init
git add .
git commit -m "New commit"
git push -u origin main
"""
 
"""
Input sempre retorna no tipo string
"""
name = input("Digite seu nome: ")
print(type(name))

"""
Atalho de operadores de atribuição
"""
num = 10
num += 1  # num = num + 1
num -= 1  # num = num - 1
num *= 1  # num = num * 1
num /= 1  # num = num / 1

"""
Operadores de string
"""
game = "The Witcher 3"
print("The Witcher" in game) # Verifica se a palavra está dentro de uma variavel

print(game[1:]) # Retorna a string a partir da 1 posição
print(game[:1]) # Retorna a string a até a 1 posição
print(game[::2]) # Retorna a string de 2 em 2 posições
print(game[::-1]) # Retorna a string de trás para frente

print(game.upper()) # Retorna tudo em Maiúsculo
print(game.lower()) # Retorna tudo em Minúsculo
print(game.title()) # Retorna a primeira letra em maiúsculo
print(game.center(30, "-")) # Retorna a string centralizada com caractere de preenchimento
print(game.find("h")) # Retorna a posição de um determinado caractere
print(game.find("e")) # Conta quantos caracteres tem em determinada variável
print(game.replace("3", "2")) # Troca uma string por outra
print(game.split(",")) # Divide os elementos com base no caractere

"""
Lista
"""
lista = ["Testando uma Lista", 2, True, "3", 2.5]
print(lista)

print(len(lista)) # Retorna o tamanho da lista
lista.append("Teste") # Adiciona um item ao final da lista
print(lista.index(2)) # Retorna o index do número 2
# lista.sort() # Ordena a lista (Não ordena STR e INT, FLOAT juntos)
print(game)
listaCopy =  lista.copy() # Copia a lista
print(listaCopy)
listaCopy.clear() # Limpa a lista
print(listaCopy)

"""
Tupla
- Não possibilita adicionar valores na tupla
- Não possibilita remover valores na tupla
- Não possibilita ordenar valores na tupla
"""
tupla = ("Testando uma Tupla", 2, True, "3", 2.5)
print(tupla)

print(tupla.index(2))

"""
Set
- Não possibilita recuperar valores no set via slice
- True e o número 1 valem a mesma coisa
- Não permite repetir valores
"""
set = {"Testando um Set", 2, True, 1, "3", 2.5}
setTeste = {"teste"}
print(set)

print(len(set))
set.update(setTeste) # Permite fazer update de outro set
set.remove(True) # Permite remover um item
print(set)

"""
Dicionarios
"""
dicionario = {
    "name": "The witcher 3",
    "yearLaunch": 2015,
    "gamePrice": 149.90,
    "classificacao": 9.5,
    "genre": ["RPG", "ação"]
}

print(dicionario["genre"]) # Recuperando um elemento do dicionário
print(dicionario.get("gamePrice")) # Outra maneira de recuperar um elemento do dicionário
print(dicionario.keys()) # Buscando apenas as chaves
print(dicionario.values()) # Buscando apenas os valores
print(dicionario.items()) # Retorna itens do dicionário como tupla de uma lista, ou seja, inclui key e a chave
dicionario["Players"] = 2
print(dicionario) # Adicionando um item no dicionário
dicionario.update({"Players": 1}) # Atualizando itens no dicionário
print(dicionario)
dicionario.pop("Players") # Removendo item no dicionário
print(dicionario)

""" 
Dicionario Aninhado
""" 
dicionarioAninhado = {
    "The witcher 3": {
        "yearLaunch": 2015,
        "classificacao": 9.5,
        "genre": ["RPG", "ação"],
    },
    "mario odyssey": {
        "yearLaunch": 2017,
        "classification": 10.0,
        "genre": ["aventura", "3d"],
    },
    "donkey kong country": {
        "yearLaunch": 1996,
        "classification": 9.5,
        "genre": ["aventura", "plataforma"],
    },
}

print(dicionarioAninhado)
print(dicionarioAninhado["mario odyssey"]["genre"]) # Buscando informação dentro de um dicionário
dicionarioAninhado["mario odyssey"]["players"] = 1 # Adicionando novo item
print(dicionarioAninhado["mario odyssey"]) 
del dicionarioAninhado["The witcher 3"] # Excluindo um dicionário
print(dicionarioAninhado)

"""
Operadores de condição
"""

# If, elif e else
num1 = 10
num2 = 20

if num1 > num2:
    print("Número 1 > Número 2")
elif num2 > num1:
    print("Número 2 > Número 1")
else:
    print("Operação inválida!")

# For
for i in range(3):
    print(i)

for i in lista:
    if i == 2:
        break # continue
    print(i)

# While
rating = 0
cont = 0
while rating != -1:
    rating = float(input("Digite a nota do jogo: "))
    if (rating != -1):
        rating += rating
        cont += 1
    rating /= cont

"""
List Comprehesion
[adicao_a_lista for váriavel_que_muda in iterable if condition == True]
"""
listNumbers = [i for i in range(10) if i < 3]
print(listNumbers)

gameList = ["The witcher 3", "Red Dead Redepemtion 2", "Black Myth: Wukong", "The Last of Us: Part 1",
            "Days Gone", "Unchearted 4"]
newList = [x for x in gameList if "a" in x]
print(newList)

"""
Funções
"""
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))

numFunc = 3
print(f"O fatorial de {numFunc} é: {factorial(numFunc)}")

"""
*args: Utilizamos ele quando não temos a certeza de quantos argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

*kwargs: Além dos valores, podemos passar também as respectivas chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total = sum_total + n
    print(f"Soma é: {sum_total}")

sum(7)
sum(8, 7)
sum(4, 5, 9)

def presentation(**data): # Data vira um dicionário
    for key, value in data.items():
        print(f"{key} - {value}")

presentation(name="Python", category="Backend", level="Iniciante")

"""
Função Lambda
É uma função anônima, ou seja, uma função sem um nome explícito, que pode ter múltiplos argumentos, mas apenas 
uma única expressão
lambda argumentos: expressão
"""
power = lambda num: num**2 # Função de potência de número
pair = lambda x: x % 2 == 0 # Função que verifica se o número é par
divNum = lambda x, y: x / y # Função que divide um número por outro
reverse = lambda s: s[::-1] # Função que inverte uma string

print(power(5))
print(pair(30))
print(divNum(10, 2))
print(reverse("Função"))

"""
Modulo
import func as nomeAlterado
from module import nomeDaFunc
"""
import os
print(os.getcwd()) # 2 - Retorna a Pasta atual
print(os.listdir())     # 3 - Lista arquivos e pastas
os.system("ver") # 4- Mostra a Versão do SO
os.system("systeminfo") # 5 - Configurações da Máquina
os.system("cls") # 6 - Limpar a tela

import webbrowser
webbrowser.open("<http://www.python.org>")

import math
print(f"{math.pi:.2f}") # Acessar o número de Pi
print(f"{math.e:.2f}") # Acessar o número de Euler
print(math.ceil(10)) # Arredondando números para cima e para baixo
print(math.factorial(7))# Fatorial de um número 
print(math.pow(5,5)) # Potênciação de números
print(math.sqrt(169)) # Raiz quadrada 
print(math.log(10)) # Logaritmo
mdc = math.gcd(25, 120) # Maior denominador comum - Reduzir frações
print(mdc)

import statistics
print(statistics.mean([3,2,3,8,9])) # Aplicar a média
print(statistics.median([1,2,3,7,8,9])) # Aplicar a mediana (Média dos dois números centrais)
print(statistics.mode([2,5,3,2,8,3,9,4,2,5,6])) # Aplicar a moda (O que mais se repete)
print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5])) # Aplicar o desvio padrão
# Medida de dispersão do conjunto, ou seja, uma medida  que indica quão uniformes são os dados do conjunto.
# - Quanto mais próximo de 0, significa que os dados do conjunto estão menos dispersos

import re
text = "OneBitCode: Transformamos pessoas em programadores sem limites"
match = re.search(r"pessoas em programadores", text) # Índice inical e final de palavras
print("Índice inicial: ", match.start())
print("Índice final: ", match.end())

site = "<https://onebitcode.com/>"
match = re.search(r"\.", site) # Buscando o índice que possui o ponto
print(match) 

padrao = "[a-m]" # Buscando uma lista de caracteres dentro de uma frase 
resultado = re.findall(padrao, text)
print(text)
print(resultado)

rule = r"^A" # Strings que começam com a letra A
phrases = ["A casa está suja", "O dia está lindo", "Vamos passear"]
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")

rule_end = r"!$" # Verifica o final de uma string $
phrases2 = "O dia está lindo!"
matches = re.search(rule_end, phrases2)
if matches:
    print("Sim, corresponde.")
else:
    print("Não corresponde.")

import random
list1 = [7, 6, 4, 3, 2, 1] 
print("Valor aleatório da lista:", random.choice(list1)) # Seleciona valor aleatório de uma lista
r1 = random.randint(5, 12) # Gera número aleatório em um intervalo de valores
print("Número aleatório entre 5 e 12:", r1)
nameCourse = "Curso Python"
r2 = random.choice(name) # Seleciona caractere aleatório de uma string
print("Caractere aleatório da string:", r2)
print("Dois valores aleatórios da lista:", random.sample(list1, 2)) # Selecionando mais de um valor aleatório, andom.sample(sequencia, tamanho)

"""
Programação Orientada a Objetos
"""
# Classes
class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes): # Passo os parametros que eu vou passar a ele depois
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes

    def __str__(self):
        return f"Filme: {self.name}"

    # Métodos
    def technical_sheet(self):
        print("-----Dados do Filme-----")
        print(f"Nome Filme: {self.name}")
        print(f"Ano Lançamento: {self.yearLaunch}")
        print(f"Está no plano? {self.includedPlan}")
        print(f"Avaliação Filme: {self.note}")
        print(f"Duração Filme: {self.durationMinutes}")

# Instancia
movie = Movie("Super Mario", 2023, False, 10.0, 120)
movie.technical_sheet()

# Encapsulamento
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # Define como privado
    
    def show(self):
        print(f"Nome: {self.name} Salário: {self.__salary}")

        # Método para buscar os dados
    def get_salary(self):
        return self.__salary
    
    # Método para alterar atributo privado
    def set_salary(self, salary):
        self.__salary = salary

fulano = Employee("Fulano", 4000)
sicrano = Employee("Sicrano", 10000)
fulano.name = "Fulano 2" # Publico
fulano.__salary = 40000 # Privado
fulano.show()
sicrano.show()

# Herança e Polimorfismo
class Phone: 
    def __init__(self,brand,model_name,price):
        self._brand = brand
        self._model_name =  model_name
        self._price =  price
    
    def __str__(self):
        return f"{self._brand}{self._model_name}"
    
    def discount(self): # Polimorfimos - Mesmo nome, coisas diferentes
        return self._price * 0.10

class SmartPhone(Phone): 
    def __init__(self,brand,model_name,price, ram, internal_memory, back_camera):  
        super().__init__(brand,model_name,price) # Pego os valores da classe pai
        
        self.ram = ram
        self.internal_memory =  internal_memory
        self.back_camera = back_camera
    
    def discount(self): # Polimorfismos - Mesmo nome, coisas diferentes
        return self._price * 0.15

Iphone = SmartPhone("Iphone","16",7000,"4GB","128GB","25MP")
print(f"Valor do {Iphone._brand}{Iphone._model_name} é {Iphone._price}")
print(vars(Iphone))
print(Iphone.discount())

"""
Arquivos
r (Leitura)
w (Escrita)
a (Append)
"""
# Escrita
name = "Alisson"
names = []
with open("4-Manipulando_Arquivos/dados/names.txt", "a", encoding="UTF-8") as file: # UTF-8 ele entender caracteres especiais
    file.write(f"{name}\n")

# Leitura
with open("dados/names.txt", "r", encoding="UTF-8") as file:
    for line in file:
        print(f"Olá {line.rstrip()}")
        names.append(line.rstrip())
    
    for name in sorted(names): # Ordena os nomes
        print(f"Olá, {name}")

import glob, os, zipfile

os.getcwd()  # Diretório atual de trabalho

for file in glob.glob("dados/*.txt"): # Lista todos os arquivos .txt
    print(file)
    
with zipfile.ZipFile("names.zip", "w") as f: # Compactando arquivos .txt
    for file in glob.glob("dados/*.txt"):
        f.write(file)
    
with zipfile.ZipFile("code.zip", "w") as f: # Compactando todos os arquivos
    for file in glob.glob("*"):
        f.write(file)
