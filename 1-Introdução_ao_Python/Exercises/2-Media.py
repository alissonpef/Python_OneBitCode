"""
Exercicio 2:
* Média de 4 notas
-> Escreva um programa em Python que leia quatro números e calcule a média entre esses números
"""

note1 = int(input("Digite a primeira nota: "))
note2 = int(input("Digite a segunda nota: "))
note3 = int(input("Digite a terceira nota: "))
note4 = int(input("Digite a quarta nota: "))

print(f"A média das quatros notas {note1}, {note2}, {note3} e {note4} é: {(note1 + note2 + note3 + note4) / 4}")