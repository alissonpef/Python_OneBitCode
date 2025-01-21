"""
Exercicio 2:
* Classe Produto e método desconto
-> Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

1. Cada produto deve ter um preço e um nome.
2. A classe deve ter um método construtor e o método dundle str.
3. A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o 
cálculo de quanto ficaria o preço final com o desconto.
"""

class Produto:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Produto: {self.name} - R$ {self.price} reais"

    def desconto(self):
        desconto = int(input("Diga a quantidade de desconto do item: "))
        desconto /= 100
        print(f"O preço do {self.name} com desconto ficou em: {self.price - (self.price * desconto)} reais")
        
ps5 = Produto("PS5", 3500)
ps5.desconto()