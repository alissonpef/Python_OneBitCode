class ContaBancaria:
    def __init__(self, numero, saldo, titular):
        self.numero = numero
        self.__saldo = saldo
        self.titular = titular

    def __str__(self):
        return f"Conta: {self.numero} - Titular: {self.titular} - Saldo: {self.getSaldo()}"

    def getSaldo(self):
        return self.__saldo

    def setSaldo(self, saldo):
        self.__saldo = saldo

    def getNomeArquivo(self):
        return f"C:/Users/Alisson Pereira/Desktop/Alisson/Programming/Python/Projeto/Dados/Conta_{self.titular}.txt"

    def deposito(self, dinheiro):
        saldoAtual = self.getSaldo()
        novoSaldo = saldoAtual + dinheiro
        self.setSaldo(novoSaldo)
        nome_arquivo = self.getNomeArquivo()
        with open(nome_arquivo, "a", encoding="UTF-8") as file:
            file.write(f"Saldo antigo: {saldoAtual}\nDepósito: {dinheiro}\nSaldo Atual: {novoSaldo}\n\n")
        print(f"Depósito na conta {self.titular} feito com sucesso!")

    def retirada(self, dinheiro):
        saldoAtual = self.getSaldo()
        if saldoAtual >= dinheiro:
            novoSaldo = saldoAtual - dinheiro
            self.setSaldo(novoSaldo)
            nome_arquivo = self.getNomeArquivo()
            with open(nome_arquivo, "a", encoding="UTF-8") as file:
                file.write(f"Saldo antigo: {saldoAtual}\nRetirada: {dinheiro}\nSaldo Atual: {novoSaldo}\n\n")
            print(f"Retirada na conta {self.titular} feita com sucesso!")
        else:
            print("Você não tem saldo suficiente!")

    def show(self):
        print(f"A conta {self.numero} de {self.titular} possui saldo: {self.getSaldo()}")

    def clear(self):
        nome_arquivo = self.getNomeArquivo()
        open(nome_arquivo, "w", encoding="UTF-8").close()

    def extrato(self):
        nome_arquivo = self.getNomeArquivo()
        print("\n-----EXTRATO DA CONTA-----\n")
        try:
            with open(nome_arquivo, "r", encoding="UTF-8") as file:
                for line in file:
                    print(line.rstrip())
        except FileNotFoundError:
            print("Nenhum extrato encontrado.")
