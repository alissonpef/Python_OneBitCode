from Conta_Bancaria import ContaBancaria
from Conta_Corrente import ContaCorrente

contaBancaria = ContaBancaria(123456, 100, "Alisson Pereira")
print(contaBancaria)
contaBancaria.show()
contaBancaria.clear()

saldo = contaBancaria.getSaldo()
print(f"Saldo inicial: {saldo}\n")

contaBancaria.deposito(100)
saldo = contaBancaria.getSaldo()
print(f"Saldo depois do deposito: {saldo}\n")

contaBancaria.retirada(200)
saldo = contaBancaria.getSaldo()
print(f"Saldo depois da retirada: {saldo}\n")

contaBancaria.retirada(100)
saldo = contaBancaria.getSaldo()
print(f"Saldo depois da retirada: {saldo}\n")

contaCorrente = ContaCorrente(5, 10)
contaCorrente.showTarifas()