"""
* Verificar conteúdo da String
-> Escreva um programa em Python para verificar se uma string contém apenas um determinado conjunto de caracteres (neste caso, a-z, A-Z e 0-9).
"""

import re

def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

text = "qweRTY012"

for i in text:
    result = re.findall("[a-z]", i) 
    if len(result) == 0:
        result = re.findall("[A-Z]", i)
        if len(result) == 0:
            result = re.findall("[0-9]", i)
            if len(result) == 0:
                print(f"O caractere '{i}' não pertence a a-z, A-Z ou 0-9!")
            else:
                print(f"O caractere '{i}' é um número: {result}")
        else:
            print(f"O caractere '{i}' é uma letra maiúscula: {result}")
    else:
        print(f"O caractere '{i}' é uma letra minúscula: {result}")

print(check_character("ABCDEFabcdef123450")) 
print(check_character("*&%@#!}{"))

