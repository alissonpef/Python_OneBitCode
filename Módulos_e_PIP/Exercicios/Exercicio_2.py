"""
* Agendamento de Desligamento PC
-> Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
"""

import os

time = int(input("Em quantos minutos voce quer que o computador desligue? \n"))
time *= 60

os.system(f"shutdown /s /t {time}")

var = input("Voce deseja cancelar o desligamento [Y/N]? \n")
if var == "Y":
    os.system("shutdown /a")
    print("Seu desligamento foi cancelado.")
else:
    print(f"Seu agendamento esta agendado para daqui a {time / 60} minutos]")

