import os


class ContaBancaria:
    def __init__(self, numero, saldo, titular):
        self.numero = numero
        self.__saldo = saldo
        self.titular = titular

    def __str__(self):
        return f"Conta: {self.numero} - Titular: {self.titular}"

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def getNomeArquivo(self):
        return f"C:/Users/Alisson Pereira/Desktop/Alisson/Programming/Python/Conta_Bancaria/Dados/Conta_{self.titular}.txt"

    def deposito(self, dinheiro):
        saldoAtual = self.getSaldo()
        novoSaldo = saldoAtual + dinheiro
        self.setSaldo(novoSaldo)
        name = self.getNomeArquivo()

        if os.path.exists(name):
            with open(name, "a", encoding="UTF-8") as file:
                file.write(
                    f"Saldo antigo: {saldoAtual} \nDepósito: {dinheiro} \nSaldo Atual: {novoSaldo}\n\n"
                )
        else:
            with open(name, "w", encoding="UTF-8") as file:
                file.write(
                    f"Saldo antigo: {saldoAtual} \nDepósito: {dinheiro} \nSaldo Atual: {novoSaldo}\n\n"
                )

        print(f"Deposito na conta {self.titular} feito com sucesso!")

    def retirada(self, dinheiro):
        saldoAtual = self.getSaldo()

        if saldoAtual >= dinheiro:
            novoSaldo = saldoAtual - dinheiro
            self.setSaldo(novoSaldo)
            name = self.getNomeArquivo()

            with open(name, "a", encoding="UTF-8") as file:
                file.write(
                    f"Saldo antigo: {saldoAtual} \nRetirada: {dinheiro} \nSaldo Atual: {novoSaldo}\n\n"
                )
            print(f"Retirada na conta {self.titular} feita com sucesso!")
        else:
            print("Você não tem saldo suficiente!")

    def show(self):
        print(
            f"A conta {self.numero} no nome de {self.titular} tem um saldo de: {self.getSaldo()}"
        )

    def clear(self):
        name = self.getNomeArquivo()
        open(name, "w")