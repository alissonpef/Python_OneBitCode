"""
* Agendamento de desligamento
-> Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
"""

import os 

# 1 - Desligar o computador em 1 min
# os.system("shutdown /s")
# os.system("shutdown /s /t 0") # Desliga imediatamente 

# 2 - Cancelar o desligamento 
# os.system("shutdown /a")

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")

def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800")

def cancel_shutdown():
    os.system("shutdown /a")

turn_off_one_hour()
cancel_shutdown()
turn_off_half_an_hour()
cancel_shutdown()